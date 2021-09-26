from .models import *
import requests, json, math
from django.db.models import Q

class RequestLogger():

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print(request.path)
        if "/admin/website/sold/" in request.path  or "/admin/website/soldmain/" in request.path:
            items = sold.objects.all().filter(order_status="NOT PAID")
            for i in items:
                data = {
                    'billCode': i.bill_code,
                    'billpaymentStatus': '0'
                }
                try:
                    req = requests.post('https://toyyibpay.com/index.php/api/getBillTransactions', data=data)
                    if json.loads(req.text)[0]['billpaymentStatus'] == "1":
                        i.order_status = "BUYING"
                        i.save()
                except:
                    print("error")

            items = sold.objects.all().filter(shipping_status="NOT PAID")
            for i in items:
                if i.shipping_bill != "":
                    data = {
                        'billCode': i.shipping_bill,
                        'billpaymentStatus': '0'
                    }
                    try:
                        req = requests.post('https://toyyibpay.com/index.php/api/getBillTransactions', data=data)
                        if json.loads(req.text)[0]['billpaymentStatus'] == "1":
                            i.shipping_status = "NOT SHIPPED"
                            i.save()
                    except:
                        print("error")

            items = sold.objects.all().filter(~Q(length=0.0, width=0.0, height=0.0, weight=0.0), air_price=0.0, sea_1_price=0.0, sea_2_price=0.0)
            for i in items:

                configurations = calc_conf.objects.all()[0]
                markup = configurations.markup / 100
                singapore_rate = configurations.singapore_rate
                singapore_sensitive_rate = configurations.singapore_sensitive_rate
                brunel_rate = configurations.brunel_rate
                brunel_sensitive_rate = configurations.brunel_sensitive_rate
                malaysia1_rate = configurations.malaysia1_rate
                malaysia1_sensitive_rate = configurations.malaysia1_sensitive_rate
                malaysia2_rate = configurations.malaysia2_rate
                malaysia2_sensitive_rate = configurations.malaysia2_sensitive_rate
                convert_rate = configurations.convert_rate
                air_number = configurations.air_number
                sea_1_number = configurations.sea_1_number
                sea_2_number = configurations.sea_2_number
                sea_1_min = configurations.sea_1_min
                sea_1_price_under_min = configurations.sea_1_price_under_min
                sea_1_price_over_min = configurations.sea_1_price_over_min
                sea_2_min = configurations.sea_2_min
                sea_2_price_under_min = configurations.sea_2_price_under_min
                sea_2_price_over_min = configurations.sea_2_price_over_min
                country = i.shipping_country

                if country == "Malaysia1":
                    normal = malaysia1_rate
                    sensitive = malaysia1_sensitive_rate
                elif country == "Malaysia2":
                    normal = malaysia2_rate
                    sensitive = malaysia2_sensitive_rate
                elif country == "Singapore":
                    normal = singapore_rate
                    sensitive = singapore_sensitive_rate
                elif country == "Brunel":
                    normal = brunel_rate
                    sensitive = brunel_sensitive_rate




                #################### AIR SHIPPING

                rate = i.shipping_rate
                length = i.length
                width = i.width
                height = i.height
                weight = i.weight
                w1 = math.ceil(float(length) * float(width) * float(height) / air_number)
                w2 = math.ceil(float(weight))
                if rate == "Normal":
                    rm = normal
                elif rate == "Sensitive":
                    rm = sensitive
                if w1 > w2:
                    air_price = w1 * rm + (w1 * rm * markup)
                else:
                    air_price = w2 * rm + (w2 * rm * markup)

                i.air_price = air_price

                #################### SEA SHIPPING

                w1 = math.ceil(float(length) * float(width) * float(height) / sea_1_number) / 10
                if w1 < sea_1_min:
                    w1 = sea_1_min


                w2 = math.ceil(float(weight))
                cbm = math.ceil(w2 / 40) / 10
                if cbm < sea_1_min:
                    cbm = sea_1_min

                if w1 > cbm:
                    sea_1_price = (w1 - sea_1_min) * sea_1_price_over_min + sea_1_price_under_min
                else:
                    sea_1_price = (cbm - sea_1_min) * sea_1_price_over_min + sea_1_price_under_min

                i.sea_1_price = sea_1_price

                #################### SEA 2 SHIPPING

                w1 = math.ceil(float(length) * float(width) * float(height) / sea_2_number)
                w2 = math.ceil(float(weight))
                if w1 < sea_2_min:
                    w1 = sea_2_min
                if w2 < sea_2_min:
                    w2 = sea_2_min
                if w1 > w2:
                    sea_2_price = (w1 - sea_2_min) * sea_2_price_over_min + sea_2_price_under_min
                else:
                    sea_2_price = (w2 - sea_2_min) * sea_2_price_over_min + sea_2_price_under_min

                i.sea_2_price = sea_2_price

                i.save()



        elif "/my_orders/" in request.path:
            items = sold.objects.all().filter(order_status="NOT PAID", client_email=request.user.email)
            for i in items:
                data = {
                    'billCode': i.bill_code,
                    'billpaymentStatus': '0'
                    }
                try:
                    req = requests.post('https://toyyibpay.com/index.php/api/getBillTransactions', data=data)
                    if json.loads(req.text)[0]['billpaymentStatus'] == "1":
                        i.order_status = "BUYING"
                        i.save()
                except:
                    pass


            items = sold.objects.all().filter(shipping_status="NOT PAID", client_email=request.user.email)
            for i in items:
                if i.shipping_bill != "":
                    data = {
                        'billCode': i.shipping_bill,
                        'billpaymentStatus': '0'
                    }
                    try:
                        req = requests.post('https://toyyibpay.com/index.php/api/getBillTransactions', data=data)
                        if json.loads(req.text)[0]['billpaymentStatus'] == "1":
                            i.shipping_status = "NOT SHIPPED"
                            i.save()
                    except:
                        pass

            items = sold.objects.all().filter(~Q(length=0.0, width=0.0, height=0.0, weight=0.0), air_price=0.0, sea_1_price=0.0, sea_2_price=0.0, client_email=request.user.email)
            for i in items:

                configurations = calc_conf.objects.all()[0]
                markup = configurations.markup / 100
                singapore_rate = configurations.singapore_rate
                singapore_sensitive_rate = configurations.singapore_sensitive_rate
                brunel_rate = configurations.brunel_rate
                brunel_sensitive_rate = configurations.brunel_sensitive_rate
                malaysia1_rate = configurations.malaysia1_rate
                malaysia1_sensitive_rate = configurations.malaysia1_sensitive_rate
                malaysia2_rate = configurations.malaysia2_rate
                malaysia2_sensitive_rate = configurations.malaysia2_sensitive_rate
                convert_rate = configurations.convert_rate
                air_number = configurations.air_number
                sea_1_number = configurations.sea_1_number
                sea_2_number = configurations.sea_2_number
                sea_1_min = configurations.sea_1_min
                sea_1_price_under_min = configurations.sea_1_price_under_min
                sea_1_price_over_min = configurations.sea_1_price_over_min
                sea_2_min = configurations.sea_2_min
                sea_2_price_under_min = configurations.sea_2_price_under_min
                sea_2_price_over_min = configurations.sea_2_price_over_min
                country = i.shipping_country
                if country == "Malaysia1":
                    normal = malaysia1_rate
                    sensitive = malaysia1_sensitive_rate
                elif country == "Malaysia2":
                    normal = malaysia2_rate
                    sensitive = malaysia2_sensitive_rate
                elif country == "Singapore":
                    normal = singapore_rate
                    sensitive = singapore_sensitive_rate
                elif country == "Brunel":
                    normal = brunel_rate
                    sensitive = brunel_sensitive_rate

                #################### AIR SHIPPING

                rate = i.shipping_rate
                length = i.length
                width = i.width
                height = i.height
                weight = i.weight
                w1 = math.ceil(float(length) * float(width) * float(height) / air_number)
                w2 = math.ceil(float(weight))
                if rate == "Normal":
                    rm = normal
                elif rate == "Sensitive":
                    rm = sensitive
                if w1 > w2:
                    air_price = w1 * rm + (w1 * rm * markup)
                else:
                    air_price = w2 * rm + (w2 * rm * markup)

                i.air_price = air_price

                #################### SEA SHIPPING

                w1 = math.ceil(float(length) * float(width) * float(height) / sea_1_number) / 10
                if w1 < sea_1_min:
                    w1 = sea_1_min


                w2 = math.ceil(float(weight))
                cbm = math.ceil(w2 / 40) / 10
                if cbm < sea_1_min:
                    cbm = sea_1_min

                if w1 > cbm:
                    sea_1_price = (w1 - sea_1_min) * sea_1_price_over_min + sea_1_price_under_min
                else:
                    sea_1_price = (cbm - sea_1_min) * sea_1_price_over_min + sea_1_price_under_min

                i.sea_1_price = sea_1_price

                #################### SEA 2 SHIPPING

                w1 = math.ceil(float(length) * float(width) * float(height) / sea_2_number)
                w2 = math.ceil(float(weight))
                if w1 < sea_2_min:
                    w1 = sea_2_min
                if w2 < sea_2_min:
                    w2 = sea_2_min
                if w1 > w2:
                    sea_2_price = (w1 - sea_2_min) * sea_2_price_over_min + sea_2_price_under_min
                else:
                    sea_2_price = (w2 - sea_2_min) * sea_2_price_over_min + sea_2_price_under_min

                i.sea_2_price = sea_2_price

                i.save()

        response = self.get_response(request)
        return response