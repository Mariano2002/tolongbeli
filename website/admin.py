from django.contrib import admin
from .models import *
from django.contrib.auth.models import Group
# Register your models here.


admin.site.site_header = "Tolongbeli Dashboard"


admin.site.unregister(Group)

@admin.register(sold)
class SoldAdmin(admin.ModelAdmin):
    list_display = ('id','linked_name', 'client_email','client_id','price', 'rmprice', 'variant', 'extra_info' ,'order_date', 'quantity', 'bill_id', 'completed')
    ordering = ('order_date',)
    search_fields = ('id','name','url','client_email','order_date','client_id',)
    list_filter = ('order_date', 'completed', 'client_email')
    list_editable = ['completed']


@admin.register(soldEditable)
class SoldEditableAdmin(admin.ModelAdmin):
    list_display = ('id', 'linked_name', 'client_id', 'order_status', 'length', 'width', 'height', 'weight', 'allow_air', 'allow_sea_1', 'allow_sea_2', 'completed')
    ordering = ('order_date',)
    search_fields = ('id','name','url','client_email','order_date','client_id',)
    list_filter = ('order_date', 'completed', 'client_email')
    list_editable = ['completed', 'length', 'width', 'height', 'weight', 'order_status', 'allow_air', 'allow_sea_1', 'allow_sea_2',]


@admin.register(new_bills)
class new_billsAdmin(admin.ModelAdmin):
    list_display = ('client_email', 'bill_code', 'price', 'description', 'bill_status',)
    search_fields = ('client_email',)
    list_filter = ('client_email',)


@admin.register(wallet)
class walletAdmin(admin.ModelAdmin):
    list_display = ('client_email', 'balance')
    search_fields = ('client_email',)
    list_filter = ('client_email',)
    list_editable = ['balance',]


@admin.register(refund)
class refundAdmin(admin.ModelAdmin):
    list_display = ('client_email', 'name', 'bank_name', 'account_number', 'value', 'completed')
    search_fields = ('client_email',)
    list_filter = ('completed',)
    list_editable = ['completed',]


@admin.register(shipping)
class shippingAdmin(admin.ModelAdmin):
    list_display = ('IDs', 'client_email', 'client_id', 'shipping_price', 'shipping_choose', 'address', 'phone', 'postcode', 'shipping_rate', 'shipping_country', 'shipping_status', 'completed')
    search_fields = ('client_email', 'sold_ids',)
    list_filter = ('completed',)
    list_editable = ['completed', 'shipping_status']