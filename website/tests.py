from django.test import TestCase
import requests
import json
from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import requests
import urllib.parse
import json
import re
from slugify import slugify
import itertools
import math
from allauth.account.signals import user_signed_up
from django.dispatch import receiver
from django.conf import settings


headers = {
    'authority': 'shopee.co.id',
    'sec-ch-ua': '^\\^Chromium^\\^;v=^\\^92^\\^, ^\\^',
    'x-shopee-language': 'id',
    'x-requested-with': 'XMLHttpRequest',
    'if-none-match-': '55b03-e7b67f19a3a3fbd30183eb93e7691cca',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
    'x-api-source': 'pc',
    'accept': '*/*',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://shopee.co.id/cart',
    'accept-language': 'en-US,en;q=0.9',
}
# 28229953.2498878504
params = (
    ('city', 'KOTA BANDUNG'),
    ('district', 'ANDIR'),
    ('itemid', '2498878504'),
    ('shopid', '28229953'),
    ('state', 'JAWA BARAT'),
    ('town', ''),
)

response = requests.get('https://shopee.co.id/api/v4/pdp/get_shipping_info', headers=headers, params=params)
print(response.text)

shipping_name = ""
shipping_price = None
for i in response.json()['data']['shipping_infos']:
    print(i['channel']['name'])
    try:
        if i['channel']['name'] == 'Reguler':
            shipping_price = int(i['original_cost'])
            shipping_name = i['channel']['name']
            break
        if int(i['original_cost']) < shipping_price:
            shipping_price = int(i['original_cost'])
            shipping_name = i['channel']['name']
    except:
        shipping_price = int(i['original_cost'])
        shipping_name = i['channel']['name']
print(shipping_price)
print(shipping_name)


input()