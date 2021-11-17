"""tolongbeli URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from website.views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home, name="home"),

    path('home', home, name="home"),

    path('shop', shop, name="catagori"),

    path('login', login_page, name="login_page"),

    path('signup', signup, name="signup"),

    path('logout', logout_page, name="logout_page"),

    path('my_orders', my_orders, name="my_orders"),

    path('calculator', calculator, name="calculator"),

    path('calculator_configuration', calculator_config, name="calculator_config"),

    path('shopee/<path:item_description>', product_page_shopee, name="product_page_shopee"),
    path('tokopedia/<path:item_description>', product_page_tokopedia, name="product_page_tokopedia"),

    path('addCart_shopee/<path:item_id>/<path:variant>/<int:quantity>', addCart_shopee, name="addCart_shopee"),
    path('addCart_tokopedia/<path:item_id>/<path:variant>/<int:quantity>', addCart_tokopedia, name="addCart_tokopedia"),

    path('removeCart/<path:item_id>', removeCart, name="removeCart"),

    path('buy', buy, name="buy"),

    path('calculate_shipping_price', calculate_shipping_price, name="calculate_shipping_price"),

    path('recharge', recharge, name="recharge"),

    path('pay_shipping', pay_shipping, name="pay_shipping"),

    path('change_bill/', change_bill, name="change_bill"),

    path('reset_password', auth_views.PasswordResetView.as_view(template_name="reset_password.html"), name="reset_password"),
    path('reset_password_sent', auth_views.PasswordResetDoneView.as_view(template_name="link_sent.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name="new_password.html"), name="password_reset_confirm"),
    path('reset_password_complete', auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_complete.html"), name="password_reset_complete"),
]
