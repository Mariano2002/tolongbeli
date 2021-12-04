from .models import *
import requests, json, math
from django.db.models import Q

class RequestLogger():

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print(request.path)
        if "/admin" in request.path  or "/admin/" in request.path:
            items = recharge_bills.objects.all().filter(bill_status="NOT PAID")

            for item in items:
                data = {
                    'billCode': item.bill_code,
                    'billpaymentStatus': '0'
                    }
                print(item.bill_code)
                req = requests.post('https://toyyibpay.com/index.php/api/getBillTransactions', data=data)
                print(json.loads(req.text)[0])
                if json.loads(req.text)[0]['billpaymentStatus'] == "1": #change all these
                            item.bill_status = "PAID"
                            item.save()
                            walleti = wallet.objects.all().filter(client_email=item.client_email)[0]
                            walleti.balance = walleti.balance + item.amount
                            walleti.save()
                            hist = history.objects.create(
                                client_email = item.client_email,
                                value = item.amount,
                                notes = "Recharge from user",
                                income = 1,
                            )
                            hist.save()

            items = order_bills.objects.all().filter(bill_status="NOT PAID", bill_code="balance")
            for item in items:
                item.bill_status = "PAID"
                item.save()
                product = cart.objects.all().filter(id=item.cart_id)[0]
                str_id = str(request.user.id)
                while len(str_id) < 6:
                    str_id = "0" + str_id

                product_buy = sold.objects.create(
                    id_product = product.id_product,
                    name = product.name,
                    price = product.price,
                    rmprice= product.rmprice,
                    variant = product.variant,
                    url = "/shopee/"+product.url,
                    client_email= product.client_email,
                    client_id= "MY"+str_id,
                    quantity= product.quantity,
                    extra_info = product.extra_info,
                    bill_id = item.id
                )
                product_buy.save()
                product.delete()
                hist = history.objects.create(
                    client_email = item.client_email,
                    value = product.rmprice,
                    notes = "Product purchase",
                    income = 0,
                )
                hist.save()


            items = shipping_bills.objects.all().filter(bill_status="NOT PAID", bill_code="balance")
            for item in items:
                item.bill_status = "PAID"
                item.save()
                product = shipping.objects.all().filter(sold_ids=item.product_ids)[0]
                str_id = str(request.user.id)
                while len(str_id) < 6:
                    str_id = "0" + str_id
                product.shipping_status = "NOT SHIPPED"
                product.save()
                hist = history.objects.create(
                    client_email = item.client_email,
                    value = product.shipping_price,
                    notes = "Shipping paid",
                    income = 0,
                )
                hist.save()


            items = order_bills.objects.all().filter(bill_status="NOT PAID")
            code_id = []
            for i in items:
                if i.bill_code not in code_id:
                    code_id.append(i.bill_code)
            print(code_id)
            for bill_code in code_id:
                data = {
                    'billCode': bill_code,
                    'billpaymentStatus': '0'
                    }
                req = requests.post('https://toyyibpay.com/index.php/api/getBillTransactions', data=data)
                if json.loads(req.text)[0]['billpaymentStatus'] == "1": #change all these
                        items = order_bills.objects.all().filter(bill_code=bill_code)
                        for item in items:
                            item.bill_status = "PAID"
                            item.save()
                            product = cart.objects.all().filter(id=item.cart_id)[0]
                            str_id = str(request.user.id)
                            while len(str_id) < 6:
                                str_id = "0" + str_id

                            product_buy = sold.objects.create(
                                id_product = product.id_product,
                                name = product.name,
                                price = product.price,
                                rmprice= product.rmprice,
                                variant = product.variant,
                                url = "/shopee/"+product.url,
                                client_email= product.client_email,
                                client_id= "MY"+str_id,
                                quantity= product.quantity,
                                extra_info = product.extra_info,
                                bill_id = item.id
                            )
                            product_buy.save()
                            product.delete()
                            hist = history.objects.create(
                                client_email = item.client_email,
                                value = product.rmprice,
                                notes = "Product purchase",
                                income = 0,
                            )
                            hist.save()

            items = shipping_bills.objects.all().filter(bill_status="NOT PAID")
            code_id = []
            for i in items:
                if i.bill_code not in code_id:
                    code_id.append(i.bill_code)
            print(code_id)

            for bill_code in code_id:
                data = {
                    'billCode': bill_code,
                    'billpaymentStatus': '0'
                    }
                req = requests.post('https://toyyibpay.com/index.php/api/getBillTransactions', data=data)
                if json.loads(req.text)[0]['billpaymentStatus'] == "1": #change all these
                        items = shipping_bills.objects.all().filter(bill_code=bill_code)
                        for item in items:
                            item.bill_status = "PAID"
                            item.save()
                            product = shipping.objects.all().filter(sold_ids=item.product_ids)[0]
                            str_id = str(request.user.id)
                            while len(str_id) < 6:
                                str_id = "0" + str_id
                            product.shipping_status = "NOT SHIPPED"
                            product.save()
                            hist = history.objects.create(
                                client_email = item.client_email,
                                value = product.shipping_price,
                                notes = "Shipping paid",
                                income = 0,
                            )
                            hist.save()

            items = new_bills.objects.all().filter(bill_status="NOT PAID")
            for i in items:
                data = {
                    'billCode': i.bill_code,
                    'billpaymentStatus': '0'
                }
                try:
                    req = requests.post('https://toyyibpay.com/index.php/api/getBillTransactions', data=data)
                    if json.loads(req.text)[0]['billpaymentStatus'] == "1":
                        i.bill_status = "PAID"
                        i.save()
                        hist = history.objects.create(
                            client_email = i.client_email,
                            value = i.price,
                            notes = "Extra bill paid",
                            income = 0,
                        )
                        hist.save()
                except:
                    pass






        elif "/my_orders" in request.path:
            items = recharge_bills.objects.all().filter(bill_status="NOT PAID", client_email=request.user.email)

            for item in items:
                data = {
                    'billCode': item.bill_code,
                    'billpaymentStatus': '0'
                    }
                req = requests.post('https://toyyibpay.com/index.php/api/getBillTransactions', data=data)
                if json.loads(req.text)[0]['billpaymentStatus'] == "1": #change all these
                            item.bill_status = "PAID"
                            item.save()
                            walleti = wallet.objects.all().filter(client_email=item.client_email)[0]
                            walleti.balance = walleti.balance + item.amount
                            walleti.save()
                            hist = history.objects.create(
                                client_email = item.client_email,
                                value = item.amount,
                                notes = "Recharge from user",
                                income = 1,
                            )
                            hist.save()

            items = order_bills.objects.all().filter(bill_status="NOT PAID", bill_code="balance", client_email=request.user.email)
            for item in items:
                item.bill_status = "PAID"
                item.save()
                product = cart.objects.all().filter(id=item.cart_id)[0]
                str_id = str(request.user.id)
                while len(str_id) < 6:
                    str_id = "0" + str_id

                product_buy = sold.objects.create(
                    id_product = product.id_product,
                    name = product.name,
                    price = product.price,
                    rmprice= product.rmprice,
                    variant = product.variant,
                    url = "/shopee/"+product.url,
                    client_email= product.client_email,
                    client_id= "MY"+str_id,
                    quantity= product.quantity,
                    extra_info = product.extra_info,
                    bill_id = item.id
                )
                product_buy.save()
                product.delete()
                hist = history.objects.create(
                    client_email = item.client_email,
                    value = product.rmprice,
                    notes = "Product purchase",
                    income = 0,
                )
                hist.save()

            items = shipping_bills.objects.all().filter(bill_status="NOT PAID", bill_code="balance", client_email=request.user.email)
            for item in items:
                item.bill_status = "PAID"
                item.save()
                product = shipping.objects.all().filter(sold_ids=item.product_ids)[0]
                str_id = str(request.user.id)
                while len(str_id) < 6:
                    str_id = "0" + str_id
                product.shipping_status = "NOT SHIPPED"
                product.save()
                hist = history.objects.create(
                    client_email = item.client_email,
                    value = product.shipping_price,
                    notes = "Shipping paid",
                    income = 0,
                )
                hist.save()



            items = order_bills.objects.all().filter(bill_status="NOT PAID", client_email=request.user.email)
            code_id = []
            for i in items:
                if i.bill_code not in code_id:
                    code_id.append(i.bill_code)
            print(code_id)
            for bill_code in code_id:
                data = {
                    'billCode': bill_code,
                    'billpaymentStatus': '0'
                    }
                req = requests.post('https://toyyibpay.com/index.php/api/getBillTransactions', data=data)
                if json.loads(req.text)[0]['billpaymentStatus'] == "1": #change all these
                        items = order_bills.objects.all().filter(bill_code=bill_code, client_email=request.user.email)
                        for item in items:
                            item.bill_status = "PAID"
                            item.save()
                            product = cart.objects.all().filter(id=item.cart_id)[0]
                            str_id = str(request.user.id)
                            while len(str_id) < 6:
                                str_id = "0" + str_id

                            product_buy = sold.objects.create(
                                id_product = product.id_product,
                                name = product.name,
                                price = product.price,
                                rmprice= product.rmprice,
                                variant = product.variant,
                                url = "/shopee/"+product.url,
                                client_email= request.user.email,
                                client_id= "MY"+str_id,
                                quantity= product.quantity,
                                extra_info = product.extra_info,
                                bill_id = item.id
                            )
                            product_buy.save()
                            product.delete()
                            hist = history.objects.create(
                                client_email = item.client_email,
                                value = product.rmprice,
                                notes = "Product purchase",
                                income = 0,
                            )
                            hist.save()

            items = shipping_bills.objects.all().filter(bill_status="NOT PAID", client_email=request.user.email)
            code_id = []
            for i in items:
                if i.bill_code not in code_id:
                    code_id.append(i.bill_code)
            print(code_id)


            for bill_code in code_id:
                data = {
                    'billCode': bill_code,
                    'billpaymentStatus': '0'
                    }
                req = requests.post('https://toyyibpay.com/index.php/api/getBillTransactions', data=data)
                print(req.text)
                if json.loads(req.text)[0]['billpaymentStatus'] == "1": #change all these
                        items = shipping_bills.objects.all().filter(bill_code=bill_code)
                        for item in items:
                            item.bill_status = "PAID"
                            item.save()
                            product = shipping.objects.all().filter(sold_ids=item.product_ids)[0]
                            str_id = str(request.user.id)
                            while len(str_id) < 6:
                                str_id = "0" + str_id
                            product.shipping_status = "NOT SHIPPED"
                            product.save()
                            hist = history.objects.create(
                                client_email = item.client_email,
                                value = product.shipping_price,
                                notes = "Shipping paid",
                                income = 0,
                            )
                            hist.save()




            items = new_bills.objects.all().filter(bill_status="NOT PAID", client_email=request.user.email)
            for i in items:
                print(i.bill_code)
                data = {
                    'billCode': i.bill_code,
                    'billpaymentStatus': '0'
                }
                try:
                    req = requests.post('https://toyyibpay.com/index.php/api/getBillTransactions', data=data)
                    print(req.text)
                    if json.loads(req.text)[0]['billpaymentStatus'] == "1":
                        i.bill_status = "PAID"
                        i.save()
                        hist = history.objects.create(
                            client_email = i.client_email,
                            value = i.price,
                            notes = "Extra bill paid",
                            income = 0,
                        )
                        hist.save()
                except:
                    pass










            # items = sold.objects.all().filter(shipping_status="NOT PAID", client_email=request.user.email)
            # for i in items:
            #     if i.shipping_bill != "":
            #         data = {
            #             'billCode': i.shipping_bill,
            #             'billpaymentStatus': '0'
            #         }
            #         try:
            #             req = requests.post('https://toyyibpay.com/index.php/api/getBillTransactions', data=data)
            #             if json.loads(req.text)[0]['billpaymentStatus'] == "1":
            #                 i.shipping_status = "NOT SHIPPED"
            #                 i.save()
            #         except:
            #             pass

        response = self.get_response(request)
        return response