from django.db import models
from django.contrib import admin
from django.utils.html import format_html
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
        ("NOT PAID", "The client hasn't pay the bill yet"),
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
    completed = models.BooleanField(null=False, blank=False, default=False)
    order_status = models.CharField(max_length=8,
                             choices=STATUS,
                             default="NOT PAID")
    quantity = models.IntegerField(default=1)
    bill_code = models.CharField(max_length=20, blank=False, default="")
    bill_new = models.BooleanField(default=False)
    length = models.FloatField(default=0)
    width = models.FloatField(default=0)
    height = models.FloatField(default=0)
    weight = models.FloatField(default=0)
    air_price = models.FloatField(default=0)
    sea_1_price = models.FloatField(default=0)
    sea_2_price = models.FloatField(default=0)
    shipping_bill = models.CharField(max_length=20, blank=False, default="")
    SHIPPING_CHOOSE = (
        ("", ""),
        ("Air", "Air"),
        ("Sea 1", "Sea 1"),
        ("Sea 2", "Sea 2"),
    )
    shipping_choose = models.CharField(max_length=5,choices=SHIPPING_CHOOSE,
                             default="")
    RATES = (
        ("Normal", "Normal"),
        ("Sensitive", "Sensitive")
    )
    shipping_rate = models.CharField(max_length=9,choices=RATES,
                             default="Normal")

    COUNTRIES = (
        ("Malaysia1", "Malaysia1"),
        ("Malaysia2", "Malaysia2"),
        ("Singapore", "Singapore"),
        ("Brunel", "Brunel"),
    )
    shipping_country = models.CharField(max_length=9,choices=COUNTRIES,
                             default="Malaysia1")
    SHIPPING_STATUS = (
        ("NOT PAID", "The client hasn't pay the bill yet"),
        ("NOT SHIPPED", "Bill has been paid, waiting to ship the product"),
        ("SHIPPED", "Order has been shipped"),
        ("ARRIVED", "Order has arrived"),
    )
    shipping_status = models.CharField(max_length=11,
                             choices=SHIPPING_STATUS,
                             default="NOT PAID")




    @admin.display
    def link(self):
        if "/shopee/" in self.url:
            self.link = str(self.url).replace("/shopee", "https://shopee.co.id")
        elif "/tokopedia/" in self.url:
            self.link = str(self.url).replace("/tokopedia", "https://www.tokopedia.com")
        return format_html(
            '<a href="{}" target="_blank">{}</a>',
            self.link,
            self.url,
        )

    def __str__(self):
        return 'Id: {0} , Name: {0} , Price: {0} , Variant: {0} , Link: {0}'.format(self.id_product, self.name, self.price, self.variant, self.url)

class soldMain(sold):

    class Meta:
        proxy = True










