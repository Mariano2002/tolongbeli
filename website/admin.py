from django.contrib import admin
from .models import *
from django.contrib.auth.models import Group
# Register your models here.


admin.site.site_header = "Dashboard"


admin.site.unregister(Group)

@admin.register(sold)
class SoldAdmin(admin.ModelAdmin):
    list_display = ('id','name','price', 'rmprice', 'change_bill', 'variant', 'link','client_email','client_id' ,'order_date', 'quantity', 'order_status', 'length', 'width', 'height', 'weight', 'shipping_rate', 'shipping_country', 'air_price', 'sea_1_price', 'sea_2_price', 'shipping_status', 'shipping_bill', 'completed')
    ordering = ('order_date',)
    search_fields = ('id','name','url','client_email','order_date','client_id',)
    list_filter = ('order_date', 'completed', 'client_email')
    list_editable = ['completed', 'order_status', 'length', 'width', 'height', 'weight', 'shipping_rate', 'air_price', 'sea_1_price', 'sea_2_price', 'shipping_country',  'shipping_status']

    def change_bill(self, obj):

        return format_html(
            "<a href=\"/change_bill/"+str(obj.id)+"\">Change Bill</a>",
        )
@admin.register(soldMain)
class SoldMainAdmin(admin.ModelAdmin):
    list_display = ('id', 'link', 'rmprice','client_id', 'order_status', 'shipping_status', 'completed')
    ordering = ('order_date',)
    search_fields = ('id','name','url','client_email','order_date','client_id',)
    list_filter = ('order_date', 'completed', 'client_email')
    list_editable = ['completed', 'order_status', 'shipping_status']

    def change_bill(self, obj):

        return format_html(
            "<a href=\"/change_bill/"+str(obj.id)+"\">Change Bill</a>",
        )