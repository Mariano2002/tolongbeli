from django.db import models
from django.contrib import admin
from django.utils.html import format_html
import json
# Create your models here.


class product_view(models.Model):
    id = models.CharField(max_length=100, blank=False, primary_key=True)
    name = models.CharField(max_length=500, blank=False)
    url = models.CharField(max_length=500, blank=False)
    price_min = models.FloatField()
    price_max = models.FloatField()
    shipping = models.FloatField()
    models = models.CharField(max_length=1000)


    def __str__(self):
        return 'Id: {0} , Name: {0} , Price: {0} , Variant: {0} , Link: {0}'.format(self.id, self.name, self.price_min, self.models, self.url)

class calc_conf(models.Model):
    markup = models.FloatField()
    singapore_rate = models.FloatField()
    singapore_sensitive_rate = models.FloatField()
    brunel_rate = models.FloatField()
    brunel_sensitive_rate = models.FloatField()
    malaysia1_rate = models.FloatField()
    malaysia1_sensitive_rate = models.FloatField()
    malaysia2_rate = models.FloatField()
    malaysia2_sensitive_rate = models.FloatField()
    convert_rate = models.FloatField()
    air_number = models.FloatField()
    sea_1_number = models.FloatField()
    sea_2_number = models.FloatField()
    sea_1_min = models.FloatField()
    sea_1_price_under_min = models.FloatField()
    sea_1_price_over_min = models.FloatField()
    sea_2_min = models.FloatField()
    sea_2_price_under_min = models.FloatField()
    sea_2_price_over_min = models.FloatField()

class sold(models.Model):
    STATUS = (
        ("CANCELLED STOCK", "Cancelled by seller did not have stock"),
        ("CANCELLED SOLD", "Cancelled by seller item sold out"),
        ("CANCELLED SHIP", "Cancelled by system seller did not shipout"),
        ("BUYING", "Bill has been paid, waiting to order the product"),
        ("ORDERED", "The product has been ordered"),
        ("SHIPPED", "Order has been shipped"),
        ("ARRIVED", "Order has arrive on the warehouse"),
    )
    id_product = models.CharField(max_length=100, blank=False, default="")
    name = models.CharField(max_length=500, blank=False)
    price = models.FloatField()
    rmprice = models.FloatField()
    variant = models.CharField(max_length=500, default="")
    url = models.CharField(max_length=500, blank=False)
    client_email = models.CharField(max_length=300, blank=False)
    client_id = models.CharField(max_length=300, blank=False, default="")
    order_date = models.DateField(null=False, blank=False, auto_now=True)
    extra_info = models.CharField(max_length=99999, default="")
    completed = models.BooleanField(null=False, blank=False, default=False)
    bill_id = models.CharField(max_length=300, blank=False)
    order_status = models.CharField(max_length=15,
                             choices=STATUS,
                             default="BUYING")
    quantity = models.IntegerField(default=1)
    length = models.FloatField(default=0)
    width = models.FloatField(default=0)
    height = models.FloatField(default=0)
    weight = models.FloatField(default=0)
    allow_air = models.BooleanField(null=False, blank=False, default=True)
    allow_sea_1 = models.BooleanField(null=False, blank=False, default=True)
    allow_sea_2 = models.BooleanField(null=False, blank=False, default=True)




    @admin.display
    def linked_name(self):
        if len(self.name) > 55:
            name = self.name[:51]+"..."
        else:
            name = self.name
        if "/shopee/" in self.url:
            self.link = str(self.url).replace("/shopee", "https://shopee.co.id")
        elif "/tokopedia/" in self.url:
            self.link = str(self.url).replace("/tokopedia", "https://www.tokopedia.com")
        return format_html(
            '<a href="{}" target="_blank">{}</a>',
            self.link,
            name,
        )

    def __str__(self):
        return 'Id: {0} , Name: {0} , Price: {0} , Variant: {0} , Link: {0}'.format(self.id_product, self.name, self.price, self.variant, self.url)


class shipping(models.Model):
    sold_ids = models.CharField(max_length=100, blank=False)
    client_email = models.CharField(max_length=300, blank=False)
    client_id = models.CharField(max_length=300, blank=False, default="")
    shipping_price = models.FloatField(default=0)
    SHIPPING_CHOOSE = (
        ("Air", "Air"),
        ("Sea 1", "Sea 1"),
        ("Sea 2", "Sea 2"),
    )
    shipping_choose = models.CharField(max_length=5, null=True,choices=SHIPPING_CHOOSE,
                             default="")
    address = models.CharField(max_length=500, blank=False, default="")
    phone = models.CharField(max_length=20, blank=False, default="")
    postcode = models.CharField(max_length=20, blank=False, default="")

    RATES = (
        ("", ""),
        ("Normal", "Normal"),
        ("Sensitive", "Sensitive")
    )
    shipping_rate = models.CharField(max_length=9,choices=RATES, null=True,
                             default="")

    COUNTRIES = (
        ("Malaysia1", "Malaysia1"),
        ("Malaysia2", "Malaysia2"),
        ("Singapore", "Singapore"),
        ("Brunel", "Brunel"),
    )
    shipping_country = models.CharField(max_length=9, null=True,choices=COUNTRIES,
                             default="")

    SHIPPING_STATUS = (
        ("NOT PAID", "The client hasn't pay the bill yet"),
        ("NOT SHIPPED", "Bill has been paid, waiting to ship the product"),
        ("SHIPPED", "Order has been shipped"),
        ("ARRIVED", "Order has arrived"),
    )
    shipping_status = models.CharField(max_length=11,
                             choices=SHIPPING_STATUS,
                             default="NOT PAID")
    completed = models.BooleanField(null=False, blank=False, default=False)

    @admin.display
    def IDs(self):
        sold_ids = ", ".join(json.loads(self.sold_ids))
        return sold_ids

class soldEditable(sold):

    class Meta:
        proxy = True

class cart(models.Model):
    RATES = (
        ("Normal", "Normal"),
        ("Sensitive", "Sensitive")
    )

    COUNTRIES = (
        ("Malaysia1", "Malaysia1"),
        ("Malaysia2", "Malaysia2"),
        ("Singapore", "Singapore"),
        ("Brunel", "Brunel"),
    )

    id_product = models.CharField(max_length=100, blank=False, default="")
    name = models.CharField(max_length=500, blank=False)
    price = models.FloatField()
    rmprice = models.FloatField()
    variant = models.CharField(max_length=500, default="")
    url = models.CharField(max_length=500, blank=False)
    client_email = models.CharField(max_length=300, blank=False)
    client_id = models.CharField(max_length=300, blank=False, default="")
    quantity = models.IntegerField(default=1)
    extra_info = models.CharField(max_length=99999, default="")

class order_bills(models.Model):
    cart_id = models.CharField(max_length=99999, blank=False)
    bill_code = models.CharField(max_length=100, blank=False)
    client_email = models.CharField(max_length=300, blank=False)
    client_id = models.CharField(max_length=300, blank=False)
    notes = models.CharField(max_length=300, blank=True, default="")
    STATUS = (
        ("PAID", "Paid"),
        ("NOT PAID", "Not paid")
    )
    bill_status = models.CharField(max_length=8,choices=STATUS,
                             default="NOT PAID")


class shipping_bills(models.Model):
    product_ids = models.CharField(max_length=99999, blank=False)
    bill_code = models.CharField(max_length=100, blank=False)
    client_email = models.CharField(max_length=300, blank=False)
    client_id = models.CharField(max_length=300, blank=False)
    notes = models.CharField(max_length=300, blank=True, default="")
    STATUS = (
        ("PAID", "Paid"),
        ("NOT PAID", "Not paid")
    )
    bill_status = models.CharField(max_length=8,choices=STATUS,
                             default="NOT PAID")




class new_bills(models.Model):
    bill_code = models.CharField(max_length=100, blank=False)
    client_email = models.CharField(max_length=300, blank=False)
    description = models.CharField(max_length=9999, blank=False)
    price = models.FloatField()
    STATUS = (
        ("PAID", "Paid"),
        ("NOT PAID", "Not paid")
    )
    bill_status = models.CharField(max_length=8,choices=STATUS,
                             default="NOT PAID")



class wallet(models.Model):
    client_email = models.CharField(max_length=300, blank=False)
    balance = models.FloatField(default=0)


class recharge_bills(models.Model):
    bill_code = models.CharField(max_length=100, blank=False)
    amount = models.FloatField(default=0)
    client_email = models.CharField(max_length=300, blank=False)
    client_id = models.CharField(max_length=300, blank=False)
    STATUS = (
        ("PAID", "Paid"),
        ("NOT PAID", "Not paid")
    )
    bill_status = models.CharField(max_length=8,choices=STATUS,
                             default="NOT PAID")


class refund(models.Model):
    client_email = models.CharField(max_length=300, blank=False)
    name = models.CharField(max_length=300, blank=False)
    bank_name = models.CharField(max_length=300, blank=False)
    account_number = models.CharField(max_length=300, blank=False)
    value = models.FloatField()
    completed = models.BooleanField(null=False, blank=False, default=False)


class history(models.Model):
    client_email = models.CharField(max_length=300, blank=False)
    value = models.FloatField()
    notes = models.CharField(max_length=300, blank=True, default="")
    in_out = models.BooleanField(null=False, blank=False, default=False)
