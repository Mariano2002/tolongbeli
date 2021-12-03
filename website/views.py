from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import requests
import urllib.parse
import json
from .models import *
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
import re
from slugify import slugify
import itertools
import math
from allauth.account.signals import user_signed_up
from django.dispatch import receiver
from django.conf import settings
from .forms import *
from datetime import datetime
import sys
import threading
import time
import logging


def check_wallet(email):
    try:
        wallet_user = wallet.objects.all().filter(client_email=email)[0]
    except:
        wallet_user = wallet.objects.create(client_email=email)
        wallet_user.save()


def user_is_not_logged_in(user):
    return not user.is_authenticated


def home(request):
    return render(request, 'index.html', {})


@csrf_exempt
def shop(request):
    if request.method == "POST":
        title = request.POST.get("Search")
        page = request.POST.get("page")
        nr_page = (int(page) - 1) * 60
        regex = re.compile(
            r'^(?:http|ftp)s?://' 
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  
            r'localhost|'
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
            r'(?::\d+)?' 
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)

        if re.match(regex, title) is not None:
            if "shopee" in title:
                try:
                    return HttpResponseRedirect('shopee/%s/' % title.split("?")[0].split("shopee.co.id/")[1])
                except:
                    r = requests.get(title)
                    return HttpResponseRedirect('shopee/%s/' % r.url.split("?")[0].split("shopee.co.id/")[1])
            elif "tokopedia" in title:
                try:
                    return HttpResponseRedirect('tokopedia/%s/' % title.split("?")[0].split("tokopedia.com/")[1])
                except:
                    headers = {
                        'Connection': 'keep-alive',
                        'sec-ch-ua': '"Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"',
                        'sec-ch-ua-mobile': '?0',
                        'sec-ch-ua-platform': '"Windows"',
                        'Upgrade-Insecure-Requests': '1',
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36',
                        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                        'Sec-Fetch-Site': 'none',
                        'Sec-Fetch-Mode': 'navigate',
                        'Sec-Fetch-User': '?1',
                        'Sec-Fetch-Dest': 'document',
                        'Accept-Language': 'en-US,en;q=0.9',
                    }

                    response = requests.get(title, headers=headers)
                    return HttpResponseRedirect('tokopedia/%s/' % response.url.split("?")[0].split("tokopedia.com/")[1])


        keyword = urllib.parse.quote(title)
        headers = {
            'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36",
            # 'cookie': cookie,
            'origin': 'https://www.tokopedia.com',
            'content-type': 'application/json',
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'referer': 'https://www.tokopedia.com/',
            'content-length': '25794'
        }
        payload = [{'operationName': 'SearchProductQueryV4', 'variables': {
            'params': f'device=desktop&page={page}&q={keyword}&rows=60&safe_search=false&scheme=https&source=search&st=product&start={nr_page}'},
                    'query': 'query SearchProductQueryV4($params: String!) {\n  ace_search_product_v4(params: $params) {\n    header {\n      totalData\n      totalDataText\n      processTime\n      responseCode\n      errorMessage\n      additionalParams\n      keywordProcess\n      __typename\n    }\n    data {\n      isQuerySafe\n      ticker {\n        text\n        query\n        typeId\n        __typename\n      }\n      redirection {\n        redirectUrl\n        departmentId\n        __typename\n      }\n      related {\n        relatedKeyword\n        otherRelated {\n          keyword\n          url\n          product {\n            id\n            name\n            price\n            imageUrl\n            rating\n            countReview\n            url\n            priceStr\n            wishlist\n            shop {\n              city\n              isOfficial\n              isPowerBadge\n              __typename\n            }\n            ads {\n              adsId: id\n              productClickUrl\n              productWishlistUrl\n              shopClickUrl\n              productViewUrl\n              __typename\n            }\n            badges {\n              title\n              imageUrl\n              show\n              __typename\n            }\n            ratingAverage\n            labelGroups {\n              position\n              type\n              title\n              url\n              __typename\n            }\n            __typename\n          }\n          __typename\n        }\n        __typename\n      }\n      suggestion {\n        currentKeyword\n        suggestion\n        suggestionCount\n        instead\n        insteadCount\n        query\n        text\n        __typename\n      }\n      products {\n        id\n        name\n        ads {\n          adsId: id\n          productClickUrl\n          productWishlistUrl\n          productViewUrl\n          __typename\n        }\n        badges {\n          title\n          imageUrl\n          show\n          __typename\n        }\n        category: departmentId\n        categoryBreadcrumb\n        categoryId\n        categoryName\n        countReview\n        discountPercentage\n        gaKey\n        imageUrl\n        labelGroups {\n          position\n          title\n          type\n          url\n          __typename\n        }\n        originalPrice\n        price\n        priceRange\n        rating\n        ratingAverage\n        shop {\n          id\n          name\n          url\n          city\n          isOfficial\n          isPowerBadge\n          __typename\n        }\n        url\n        wishlist\n        sourceEngine: source_engine\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n'}]
        res = requests.post('https://gql.tokopedia.com/', headers=headers, json=payload)
        listi = json.loads(res.text[1:-1])
        context_tokopedia = {}
        for product in listi['data']['ace_search_product_v4']['data']['products']:
            context_tokopedia[product['id']] = {"name": product['name'],
                                                "image": product['imageUrl'],
                                                "price": int(int(product['price'].replace("Rp","").replace(".",""))+(int(product['price'].replace("Rp","").replace(".",""))*0.1)),
                                                "rating": int(product['rating']),
                                                "url": product['url'].split("?")[0].replace("https://www.tokopedia.com/","").encode('unicode_escape').decode("utf-8") , }



        headers = {
            'authority': 'shopee.co.id',
            'x-shopee-language': 'id',
            'x-requested-with': 'XMLHttpRequest',
            'if-none-match-': '55b03-4e446b2d664c59be19b64028428c4228',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36',
            'x-api-source': 'pc',
            'accept': '*/*',
            'sec-gpc': '1',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': f'https://shopee.co.id/search?keyword={keyword}',
            'accept-language': 'en-US,en;q=0.9',
        }
        params = (('by', 'relevancy'),
            ('keyword', f'{title}'),
            ('limit', '60'),
            ('newest', str(nr_page)),
            ('order', 'desc'),
            ('page_type', 'search'),
            ('scenario', 'PAGE_GLOBAL_SEARCH'),
            ('version', '2'),)
        response = requests.get('https://shopee.co.id/api/v4/search/search_items', headers=headers, params=params)
        context_shopee = {}

        for product in response.json()['items']:
            # price_1 = str(int(int(product['item_basic']['price'])/100000))[::-1]
            # price_2 = ''
            # while price_1:
            #     price_2 += price_1[:3]
            #     if len(price_1) > 3:
            #         price_2 += '.'
            #     price_1 = price_1[3:]
            price_2 = int(int(int(product['item_basic']['price'])/100000) + (int(int(product['item_basic']['price'])/100000)*0.1))
            context_shopee[product['item_basic']['itemid']] = {"name": product['item_basic']['name'],
                                                               "image": "https://cf.shopee.co.id/file/" + product['item_basic']['image'],
                                                               # "price": price_2[::-1],
                                                               "price": price_2,
                                                               "rating": int(product['item_basic']['item_rating']['rating_star']),
                                                               "url": str("-".join(product['item_basic']['name'].split(" ")) + "-i." + str(product['item_basic']['shopid']) + "." + str(product['item_basic']['itemid'])).encode('unicode_escape').decode("utf-8") , }

        context = {'title': title, 'page': int(page), 'next': int(page)+1, 'previous': int(page)-1, 'context_tokopedia': context_tokopedia, 'context_shopee': context_shopee, 'list_numbers': [1,2,3,4,5]}

        return render(request, 'shop.html', context)
    else:
        return render(request, 'shop.html', {})


@user_passes_test(user_is_not_logged_in, login_url=home)
def login_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            check_wallet(request.user.email)
            return redirect(home)
        else:
            messages.info(request, 'Username or password in incorrect')
            return render(request, 'login.html', {})
    else:
        return render(request, 'login.html', {})


@user_passes_test(user_is_not_logged_in, login_url=home)
def signup(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, f'Account was created for {user}')
            return redirect(login_page)
    context = {"form":form}
    return render(request, 'registration.html', context)


def logout_page(request):
    logout(request)
    return redirect(login_page)


def product_page_shopee(request, item_description):

    headers = {
        'authority': 'shopee.co.id',
        'x-shopee-language': 'id',
        'x-requested-with': 'XMLHttpRequest',
        'af-ac-enc-dat': 'AAEAAAF6z/wDGgAAAAACQQAAAAAAAAAAtMuVi2/+Dve5XjZC8M1ZPpCceXZbZqo10I+PP7QMrRb3fT+aD0RSs87TJszd7g5ZmsCtN5HQr99bLioncG2pELRCHh0Lq/lK8Y84A9mhmamKO/VGe++CIRsdE1FTkp/Gn3vl0CdM8QCRM8hAyW43KYeqXB3a1sb5S3wtch1whw+8b5tUfoB1wbAKQNK/AmEFtjIeEKPwr4xCyEzqRuoKcGBgoGViDEF3cCxtm1GHD6EIF1MbxzwmFN+yD89JjfMMk9L8VGSnEueC1EAOGDYjjTRMD+NdT+3ycyG2O626HdINsT7of3gKd4bvnDul33CBfVBArT14/rwkD+teUjoce0wjRLJEuSux5JEY0SWxFQHYu5venhj5CM9rCVNrDmBR07I5PbqTu9FTrRJYO5MOu6IRXPuJ7sGzmRpUp5/uSk4/4rQpDJWlTrKf72hgFwV1V+cY+E6mh8wt7m1824vj7HXqRq4v4PlogiT6JH0tOwNbe3bTBTYq2zR6PRw/FJWCQDA7zV94v/i6pXbnQ2DAOHfLGvFo+ie21Vfv8ZcbOvyaSwVgo63gkD6Hi7NqhmotT14xBhlstwzFVbpGSg7PtuSzaM/FaB8SRSZLWP7MGJWQSTNfOVSaKdmrHu6LLPx/Gnz0d9XzL1eGhywBIRq+R5f/NhMnw8f21UXD2mkb2JsAQ8Y9lVW9cL3Wx1rWu2p1YyWapvY/M5Cfgn9CDEAEMpf/NhMnw8f21UXD2mkb2JtG+3aD8HYoOSinvuEbrEDSQrdh9zsjKT0zW53MYbrKpw==',
        'if-none-match-': '55b03-1ff68174aaa4385f1de36256e9c910c4',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36',
        'x-api-source': 'pc',
        'accept': '*/*',
        'sec-gpc': '1',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': f'https://shopee.co.id/{item_description}'.encode('unicode_escape').decode("utf-8"),
        'accept-language': 'en-US,en;q=0.9',
        'if-none-match': '1bdac07452c0da90a6d8e6e48af99a6d',
    }

    params = (
        ('itemid', item_description.split(".")[-1].replace("/","")),
        ('shopid',  item_description.split(".")[-2].replace("/","")),
    )

    response = requests.get('https://shopee.co.id/api/v2/item/get', headers=headers, params=params)

    product = response.json()['item']
    product['videos'] = []
    for nr, video in enumerate(product['video_info_list']):
        product['videos'].append(product['video_info_list'][nr]['video_id'])

    def convert_price(price1):
        price_1 = price1[::-1]
        price_2 = ''
        while price_1:
            price_2 += price_1[:3]
            if len(price_1) > 3:
                price_2 += '.'
            price_1 = price_1[3:]
        return price_2[::-1]

    # models = []
    # for model in product['models']:
    #     models.append({"name":model['name'],"price":convert_price(str(int(int(model['price'])/100000))),"stock":model['normal_stock'],})

    models = []
    for model in product['models']:
        models.append({"name":model['name'],"price":int(int(model['price'])/100000+(int(model['price'])/100000*0.1)),"stock":model['normal_stock'],})

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

    params = (
        ('city', 'KOTA BANDUNG'),
        ('district', 'ANDIR'),
        ('itemid', item_description.split(".")[-1].replace("/","")),
        ('shopid', item_description.split(".")[-2].replace("/","")),
        ('state', 'JAWA BARAT'),
        ('town', ''),
    )

    response = requests.get('https://shopee.co.id/api/v4/pdp/get_shipping_info', headers=headers, params=params)

    shipping_name = ""
    shipping_price = None
    for i in response.json()['data']['shipping_infos']:
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

    for nr,i in enumerate(product['images']):
        product['images'][nr] = "https://cf.shopee.co.id/file/"+product['images'][nr]


    context_product_shopee = {   "id": product['itemid'],
                                 "url": f"https://shopee.co.id/{item_description}",
                                 "name": product['name'],
                                 "images": product['images'],
                                 "image": "https://cf.shopee.co.id/file/"+product['image'],
                                 "videos": product['videos'],
                                 "item_rating": product['item_rating']['rating_star'],
                                 "price_min": int(int(product['price_min'])/100000+(int(product['price_min'])/100000*0.1)),
                                 "price_max": int(int(product['price_max'])/100000+(int(product['price_max'])/100000*0.1)),
                                 "description": product['description'],
                                 "models": models,
                                 "shop_location": product['shop_location'],
                                 "shipping": int(int(shipping_price/100000)+(int(shipping_price/100000)*0.1)),
                                 }
    try:
        product_obj = product_view.objects.create(
            id = product['itemid'],
            name = product['name'],
            url = item_description,
            price_min = int(int(product['price_min'])/100000+(int(product['price_min'])/100000*0.1)),
            price_max = int(int(product['price_max'])/100000+(int(product['price_max'])/100000*0.1)),
            shipping = int(int(shipping_price/100000)+(int(shipping_price/100000)*0.1)),
            models = json.dumps(models),
        )
        product_obj.save()
    except:
        product_view.objects.filter(id=product['itemid']).delete()
        product_obj = product_view.objects.create(
            id = product['itemid'],
            name = product['name'],
            url = item_description,
            price_min = int(int(product['price_min'])/100000+(int(product['price_min'])/100000*0.1)),
            price_max = int(int(product['price_max'])/100000+(int(product['price_max'])/100000*0.1)),
            shipping = int(int(shipping_price/100000)+(int(shipping_price/100000)*0.1)),
            models = json.dumps(models),
        )
        product_obj.save()

    return render(request, 'product_page.html', context_product_shopee)


def product_page_tokopedia(request, item_description):
    global prods
    import json
    def convert_price(price1):
        price_1 = price1[::-1]
        price_2 = ''
        while price_1:
            price_2 += price_1[:3]
            if len(price_1) > 3:
                price_2 += '.'
            price_1 = price_1[3:]
        return price_2[::-1]
    # options = Options()
    # # options.add_argument('--headless')
    # driver = selenium.webdriver.Chrome(options=options)
    # driver.get("https://www.tokopedia.com/")
    # # driver.get("https://www.tokopedia.com/jeantboutique/promo-baju-atasan-kemeja-blouse-valery-wanita-lengan-panjang-murah")
    # # time.sleep(5)
    # request_cookies_browser = driver.get_cookies()
    # driver.quit()
    # s = requests.Session()
    # # passing the cookies generated from the browser to the session
    # c = [s.cookies.set(c['name'], c['value']) for c in request_cookies_browser]
    #


    def getProxy():
        try:
            r = requests.get(proxy_url, timeout=5)
            js = json.loads(r.text)
            #, js['randomUserAgent']
            return js['proxy']
        except Exception as e:
            pass

    api_key = "jJcauPNv4W2rg75x3tHGsbVqZAyLCpEY"
    proxy_url = "http://falcon.proxyrotator.com:51337/?apiKey={}&userAgent=true&get=true".format(api_key)

    prods = ""

    class StoppableThread(threading.Thread):
        """Thread class with a stop() method. The thread itself has to check
        regularly for the stopped() condition."""

        def __init__(self):
            super(StoppableThread, self).__init__()
            self._stopper = threading.Event()  # ! must not use _stop

        def stopit(self):  # (avoid confusion)
            self._stopper.set()  # ! must not use _stop

        def stopped(self):
            return self._stopper.is_set()  # ! must not use _stop

    class datalogger(StoppableThread):
        """
        """

        import time

        def __init__(self, outfile):
            """
            """
            StoppableThread.__init__(self)
            self.outfile = outfile

        def run(self):
            global prods

            while not self.stopped():
                try:
                    headers = {
                        'authority': 'gql.tokopedia.com',
                        'sec-ch-ua': '^\\^Chromium^\\^;v=^\\^92^\\^, ^\\^',
                        'x-version': '27ca28b',
                        'sec-ch-ua-mobile': '?0',
                        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
                        'content-type': 'application/json',
                        'accept': '*/*',
                        'x-source': 'tokopedia-lite',
                        'x-device': 'desktop',
                        'x-tkpd-lite-service': 'zeus',
                        'x-tkpd-akamai': 'pdpGetLayout',
                        'origin': 'https://www.tokopedia.com',
                        'sec-fetch-site': 'same-site',
                        'sec-fetch-mode': 'cors',
                        'sec-fetch-dest': 'empty',
                        'referer': f'https://www.tokopedia.com/{item_description}'.encode('unicode_escape').decode("utf-8"),
                        'accept-language': 'en-US,en;q=0.9',
                    }
                    s = requests.Session()
                    # proxy = getProxy()
                    # proxies = {'https': 'https://' + proxy}

                    req = s.get(f"https://www.tokopedia.com/{item_description}".encode('unicode_escape').decode("utf-8"),
                        headers=headers,
                        # proxies=proxies,
                        timeout=5)


                    cookies = ""
                    for c in s.cookies.get_dict():
                        cookies = cookies + c + "=" + s.cookies.get_dict()[c] + "; "

                    shopDomain = item_description.split("/")[0]
                    productKey = item_description.split("/")[1]
                    payload = [
                        {
                            "operationName": "PDPGetLayoutQuery",
                            "variables": {
                                "shopDomain": shopDomain,
                                "productKey": productKey,
                                "layoutID": "",
                                "apiVersion": 1,
                                "userLocation": {
                                    "addressID": "0",
                                    "districtID": "2166",
                                    "postalCode": "",
                                    "latlon": ""
                                }
                            },
                            "query": "fragment ProductVariant on pdpDataProductVariant {\n  errorCode\n  parentID\n  defaultChild\n  sizeChart\n  variants {\n    productVariantID\n    variantID\n    name\n    identifier\n    option {\n      picture {\n        urlOriginal: url\n        urlThumbnail: url100\n        __typename\n      }\n      productVariantOptionID\n      variantUnitValueID\n      value\n      hex\n      __typename\n    }\n    __typename\n  }\n  children {\n    productID\n    price\n    priceFmt\n    optionID\n    productName\n    productURL\n    picture {\n      urlOriginal: url\n      urlThumbnail: url100\n      __typename\n    }\n    stock {\n      stock\n      isBuyable\n      stockWording\n      stockWordingHTML\n      minimumOrder\n      maximumOrder\n      __typename\n    }\n    isCOD\n    isWishlist\n    campaignInfo {\n      campaignID\n      campaignType\n      campaignTypeName\n      campaignIdentifier\n      background\n      discountPercentage\n      originalPrice\n      discountPrice\n      stock\n      stockSoldPercentage\n      threshold\n      startDate\n      endDate\n      endDateUnix\n      appLinks\n      isAppsOnly\n      isActive\n      hideGimmick\n      isCheckImei\n      __typename\n    }\n    thematicCampaign {\n      additionalInfo\n      background\n      campaignName\n      icon\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment ProductMedia on pdpDataProductMedia {\n  media {\n    type\n    urlThumbnail: URLThumbnail\n    videoUrl: videoURLAndroid\n    prefix\n    suffix\n    description\n    __typename\n  }\n  videos {\n    source\n    url\n    __typename\n  }\n  __typename\n}\n\nfragment ProductHighlight on pdpDataProductContent {\n  name\n  price {\n    value\n    currency\n    __typename\n  }\n  campaign {\n    campaignID\n    campaignType\n    campaignTypeName\n    campaignIdentifier\n    background\n    percentageAmount\n    originalPrice\n    discountedPrice\n    originalStock\n    stock\n    stockSoldPercentage\n    threshold\n    startDate\n    endDate\n    endDateUnix\n    appLinks\n    isAppsOnly\n    isActive\n    hideGimmick\n    __typename\n  }\n  thematicCampaign {\n    additionalInfo\n    background\n    campaignName\n    icon\n    __typename\n  }\n  stock {\n    useStock\n    value\n    stockWording\n    __typename\n  }\n  variant {\n    isVariant\n    parentID\n    __typename\n  }\n  wholesale {\n    minQty\n    price {\n      value\n      currency\n      __typename\n    }\n    __typename\n  }\n  isCashback {\n    percentage\n    __typename\n  }\n  isTradeIn\n  isOS\n  isPowerMerchant\n  isWishlist\n  isCOD\n  isFreeOngkir {\n    isActive\n    __typename\n  }\n  preorder {\n    duration\n    timeUnit\n    isActive\n    preorderInDays\n    __typename\n  }\n  __typename\n}\n\nfragment ProductCustomInfo on pdpDataCustomInfo {\n  icon\n  title\n  isApplink\n  applink\n  separator\n  description\n  __typename\n}\n\nfragment ProductInfo on pdpDataProductInfo {\n  row\n  content {\n    title\n    subtitle\n    applink\n    __typename\n  }\n  __typename\n}\n\nfragment ProductDetail on pdpDataProductDetail {\n  content {\n    title\n    subtitle\n    applink\n    showAtFront\n    isAnnotation\n    __typename\n  }\n  __typename\n}\n\nfragment ProductDataInfo on pdpDataInfo {\n  icon\n  title\n  isApplink\n  applink\n  content {\n    icon\n    text\n    __typename\n  }\n  __typename\n}\n\nfragment ProductSocial on pdpDataSocialProof {\n  row\n  content {\n    icon\n    title\n    subtitle\n    applink\n    type\n    rating\n    __typename\n  }\n  __typename\n}\n\nquery PDPGetLayoutQuery($shopDomain: String, $productKey: String, $layoutID: String, $apiVersion: Float, $userLocation: pdpUserLocation!) {\n  pdpGetLayout(shopDomain: $shopDomain, productKey: $productKey, layoutID: $layoutID, apiVersion: $apiVersion, userLocation: $userLocation) {\n    name\n    pdpSession\n    basicInfo {\n      alias\n      id: productID\n      shopID\n      shopName\n      minOrder\n      maxOrder\n      weight\n      weightUnit\n      condition\n      status\n      url\n      needPrescription\n      catalogID\n      isLeasing\n      isBlacklisted\n      menu {\n        id\n        name\n        url\n        __typename\n      }\n      category {\n        id\n        name\n        title\n        breadcrumbURL\n        isAdult\n        detail {\n          id\n          name\n          breadcrumbURL\n          isAdult\n          __typename\n        }\n        __typename\n      }\n      blacklistMessage {\n        title\n        description\n        button\n        url\n        __typename\n      }\n      txStats {\n        transactionSuccess\n        transactionReject\n        countSold\n        paymentVerified\n        itemSoldPaymentVerified\n        __typename\n      }\n      stats {\n        countView\n        countReview\n        countTalk\n        rating\n        __typename\n      }\n      __typename\n    }\n    components {\n      name\n      type\n      position\n      data {\n        ...ProductMedia\n        ...ProductHighlight\n        ...ProductInfo\n        ...ProductDetail\n        ...ProductSocial\n        ...ProductDataInfo\n        ...ProductCustomInfo\n        ...ProductVariant\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n"
                        }
                    ]
                    data = json.dumps(payload)

                    headers = {
                        'authority': 'gql.tokopedia.com',
                        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
                        'content-type': 'application/json',
                        'accept': '*/*',
                        'x-source': 'tokopedia-lite',
                        'x-device': 'desktop',
                        'x-tkpd-lite-service': 'zeus',
                        'x-tkpd-akamai': 'pdpGetLayout',
                        'sec-gpc': '1',
                        'sec-fetch-site': 'same-site',
                        'sec-fetch-mode': 'cors',
                        'sec-fetch-dest': 'empty',
                        'accept-language': 'en-US,en;q=0.9',
                        # 'cookie': '_UUID_NONLOGIN_=f27a4fbb262751e7f59cedf8dc20b920; _UUID_NONLOGIN_.sig=Hp9ftFod1XGVPNEK3WDmqDWE5q0; DID=8f0b5ee08e63d5cb01508be397b525c65bcd51c937be8234c059aa99f503354617e297c8fc05e9f1fb2295013657811f; DID_JS=OGYwYjVlZTA4ZTYzZDVjYjAxNTA4YmUzOTdiNTI1YzY1YmNkNTFjOTM3YmU4MjM0YzA1OWFhOTlmNTAzMzU0NjE3ZTI5N2M4ZmMwNWU5ZjFmYjIyOTUwMTM2NTc4MTFm47DEQpj8HBSa+/TImW+5JCeuQeRkm5NMpJWZG3hSuFU=; bm_sz=F9145F22A84092AE45098162BE41E752~YAAQyxXfrQ6Bw299AQAANENQcw0lHAlP/a4QIoJU/lXcUsu6EHSuzGHjOM+PmG58gk10toRJx4msMpBA0tzo06HCHrIIa7atASFzlh+KHgPDWqak/++5RtNeO1CXqixDgC9CWrBsP4fYVJrkhFa5PJhQm7aSytbzMrHI7MFl+i1pQsDAV//YBO+rEOW/9SrsWKhAKwLsr0Vv1TvZSZIrtbE8DWnvTZUjjVE8+/nXV3NcRtd+RA8KBerOAGUV3V/oxs40Dd2gM/2ELaARDMFCMT73DRi4LgezL+K5KnDfSSsqI2qLMbQ=~3553590~3553605; ak_bmsc=2BBDE757975D4CF99A09EA1AD2C0DFC4~000000000000000000000000000000~YAAQyxXfrRKBw299AQAABUhQcw1GryNoOdTWDnzQ4l4lUsbLOHmnRHq1nQlFy853A4eflrcZ8GRNEQw0foAbbL/VHnDITJctNzyzJykPESU9NkZI50QO4fQsMQHKo88T3cu2woTfFA4wzOmhVD5CgX64/wmDMZ9akNSn9B2kZe5CGVrRglt1fdYmvUqszRvuTFWDiuRjR01qFEuM7c2cJsFfYOJzcvIZSp09VJgR0DeT46afu/mYgUWjj+dL3PtLSDutR2OV5omUuwwpBn0Br0Ctb1/LE7mnX3Q691gwQwoqK8BnaijqvW/4R7bjs1HFziwL4bmjxc+NAhP7UB23f1ZDkzLcxvdlYH4OuGZ2UpDcoTgC29MZrujJoOstfiBU0iUPlyArQZUP4n4=; _SID_Tokopedia_=6urEQcgCufTbcWGpI0cenOH09URIJ2UVPaSj5ZzekBjBjnIwbphisip2GWjHJqwIaNPigHfMloug2FQzdA7KPw8DViiglzNB6tXOyAr-6qI5DUG0nNBM25Ex06-mfb2G; bm_mi=D79F8510FAC49A3D10EDBAD68A5BB773~3KijlFBSRlacbn5kji77g0IhUjcVk5yzG4p3363nDAj+bjI5GsDJJjNS129U+Uca/ElkjQXFbrbxoqMoJawWslkyHz/G4GBK2w5+PZhFIzJhE1ISWHiMTykeWGnANtD15ipjyxDwFHbPqiimfMFhegFz/w5TSinlD6goC8hyI/ZODj8CSzvMg4Kstd0uZJ/fhd+7MPHdIy7gwM0qfGf7wbKkXA+fXaoOnj4ofMcmhNjtYHOEmPdsq+OlSZPBDk7Izk2a4pd2K9xQOISqp9D3h5e2ggu07FjN90mwAPZQzCUbd9VZT17DD2Ez8i04p8fl9U7lJUhym5baY4QK/q42AA==; bm_sv=3C1C919EF5958BA72D073627E7C76C64~CwDH6TXXmBNzH2A0W9m5ryAIzii7pZYUfiUkAEIBoWJmNtBtxzgLeu3WzmsredzMOZPBejM8VCmOR+zJyNT05ikK8QGZ7tXgiG8beB8DA3Xk1iDw1evp1XF0tiLeAXR/ULCBsc4XKXlzzv10MZgCZ+5u5asNqUwCzol2BsEqWRw=; _CAS_={"dId":2274,"aId":0,"lbl":"Jakarta Pusat","cId":176,"long":"","lat":"","pCo":"","wId":12210375,"sId":11530573}; _abck=0606DF49F4D1546D546D50EC3EA27A65~0~YAAQzRXfrSudsjJ9AQAAXh9bcwaY1aAc2sWbjUB7RlpY9ywwofQRkUqt0cSUQaC/7X6AUR3ailJJlxajA0q+DHX09B5kSB/+URG+wKZlg5prYD9JjvnLJNbETmirl0xa0RaoRN+eu2L5Y9TmA/U0mFJgO1+M8cpo38uD6bSMieVWzOKjvlr62Mz54gKlmBefqguV72suk0rOSZnGHaL6HWqm3a++q0iHhmv8aNpmfoB9ECz/3JW1PHtbdq/K2sM5VvbNEH9v3Dk6zA3zfrZDMjKIlHSz/lbVvy7DL/lDstk7fj8FwHs2YhsFqasq/yjbUW1BUSweSt1qvlTOU8keElGjcWZpYrb4buQsESvonNXxNEdzKCq8hq9GJc1Bx1xJ0yH8tV/+cziVZLEfCGH4FmEjiv/P/vPVTLbG~-1~-1~-1; hfv_banner=true',

                        'cookie': cookies,
                    }
                    # while True:
                    # try:
                    #     proxy = getProxy()
                    #     break
                    # except:
                    #     pass

                    # proxies = {'https': 'https://'+proxy}
                    if self.stopped():
                        break

                    resi = requests.post('https://gql.tokopedia.com/', headers=headers, data=data, timeout=2)
                    prods = resi.text
                    products = json.loads(prods[1:-1])
                    weight = int(str(products['data']['pdpGetLayout']['basicInfo']['weight']))/1000
                    res = resi
                except:
                    pass

    threads = []
    for i in range(0, 15):
        test = datalogger("test.txt")
        threads.append(test)
        test.start()
    while prods == "":
        pass
    for i in threads:
        i.stopit()

    '''while True:
        try:
            headers = {
                'authority': 'gql.tokopedia.com',
                'sec-ch-ua': '^\\^Chromium^\\^;v=^\\^92^\\^, ^\\^',
                'x-version': '27ca28b',
                'sec-ch-ua-mobile': '?0',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
                'content-type': 'application/json',
                'accept': '*/*',
                'x-source': 'tokopedia-lite',
                'x-device': 'desktop',
                'x-tkpd-lite-service': 'zeus',
                'x-tkpd-akamai': 'pdpGetLayout',
                'origin': 'https://www.tokopedia.com',
                'sec-fetch-site': 'same-site',
                'sec-fetch-mode': 'cors',
                'sec-fetch-dest': 'empty',
                'referer': f'https://www.tokopedia.com/' + item_description,
                'accept-language': 'en-US,en;q=0.9',
            }

            s = requests.Session()
            # proxy = getProxy()
            # proxies = {'https': 'https://' + proxy}
            req = s.get(
                "https://www.tokopedia.com/"+item_description,
                headers=headers,
                # proxies=proxies,
                timeout=5)

            cookies = ""
            for c in s.cookies.get_dict():
                cookies = cookies + c + "=" + s.cookies.get_dict()[c] + "; "



            shopDomain = item_description.split("/")[0]
            productKey = item_description.split("/")[1]
            payload = [
                    {
                        "operationName": "PDPGetLayoutQuery",
                        "variables": {
                            "shopDomain": shopDomain,
                            "productKey": productKey,
                            "layoutID": "",
                            "apiVersion": 1,
                            "userLocation": {
                                "addressID": "0",
                                "districtID": "2166",
                                "postalCode": "",
                                "latlon": ""
                            }
                        },
                        "query": "fragment ProductVariant on pdpDataProductVariant {\n  errorCode\n  parentID\n  defaultChild\n  sizeChart\n  variants {\n    productVariantID\n    variantID\n    name\n    identifier\n    option {\n      picture {\n        urlOriginal: url\n        urlThumbnail: url100\n        __typename\n      }\n      productVariantOptionID\n      variantUnitValueID\n      value\n      hex\n      __typename\n    }\n    __typename\n  }\n  children {\n    productID\n    price\n    priceFmt\n    optionID\n    productName\n    productURL\n    picture {\n      urlOriginal: url\n      urlThumbnail: url100\n      __typename\n    }\n    stock {\n      stock\n      isBuyable\n      stockWording\n      stockWordingHTML\n      minimumOrder\n      maximumOrder\n      __typename\n    }\n    isCOD\n    isWishlist\n    campaignInfo {\n      campaignID\n      campaignType\n      campaignTypeName\n      campaignIdentifier\n      background\n      discountPercentage\n      originalPrice\n      discountPrice\n      stock\n      stockSoldPercentage\n      threshold\n      startDate\n      endDate\n      endDateUnix\n      appLinks\n      isAppsOnly\n      isActive\n      hideGimmick\n      isCheckImei\n      __typename\n    }\n    thematicCampaign {\n      additionalInfo\n      background\n      campaignName\n      icon\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment ProductMedia on pdpDataProductMedia {\n  media {\n    type\n    urlThumbnail: URLThumbnail\n    videoUrl: videoURLAndroid\n    prefix\n    suffix\n    description\n    __typename\n  }\n  videos {\n    source\n    url\n    __typename\n  }\n  __typename\n}\n\nfragment ProductHighlight on pdpDataProductContent {\n  name\n  price {\n    value\n    currency\n    __typename\n  }\n  campaign {\n    campaignID\n    campaignType\n    campaignTypeName\n    campaignIdentifier\n    background\n    percentageAmount\n    originalPrice\n    discountedPrice\n    originalStock\n    stock\n    stockSoldPercentage\n    threshold\n    startDate\n    endDate\n    endDateUnix\n    appLinks\n    isAppsOnly\n    isActive\n    hideGimmick\n    __typename\n  }\n  thematicCampaign {\n    additionalInfo\n    background\n    campaignName\n    icon\n    __typename\n  }\n  stock {\n    useStock\n    value\n    stockWording\n    __typename\n  }\n  variant {\n    isVariant\n    parentID\n    __typename\n  }\n  wholesale {\n    minQty\n    price {\n      value\n      currency\n      __typename\n    }\n    __typename\n  }\n  isCashback {\n    percentage\n    __typename\n  }\n  isTradeIn\n  isOS\n  isPowerMerchant\n  isWishlist\n  isCOD\n  isFreeOngkir {\n    isActive\n    __typename\n  }\n  preorder {\n    duration\n    timeUnit\n    isActive\n    preorderInDays\n    __typename\n  }\n  __typename\n}\n\nfragment ProductCustomInfo on pdpDataCustomInfo {\n  icon\n  title\n  isApplink\n  applink\n  separator\n  description\n  __typename\n}\n\nfragment ProductInfo on pdpDataProductInfo {\n  row\n  content {\n    title\n    subtitle\n    applink\n    __typename\n  }\n  __typename\n}\n\nfragment ProductDetail on pdpDataProductDetail {\n  content {\n    title\n    subtitle\n    applink\n    showAtFront\n    isAnnotation\n    __typename\n  }\n  __typename\n}\n\nfragment ProductDataInfo on pdpDataInfo {\n  icon\n  title\n  isApplink\n  applink\n  content {\n    icon\n    text\n    __typename\n  }\n  __typename\n}\n\nfragment ProductSocial on pdpDataSocialProof {\n  row\n  content {\n    icon\n    title\n    subtitle\n    applink\n    type\n    rating\n    __typename\n  }\n  __typename\n}\n\nquery PDPGetLayoutQuery($shopDomain: String, $productKey: String, $layoutID: String, $apiVersion: Float, $userLocation: pdpUserLocation!) {\n  pdpGetLayout(shopDomain: $shopDomain, productKey: $productKey, layoutID: $layoutID, apiVersion: $apiVersion, userLocation: $userLocation) {\n    name\n    pdpSession\n    basicInfo {\n      alias\n      id: productID\n      shopID\n      shopName\n      minOrder\n      maxOrder\n      weight\n      weightUnit\n      condition\n      status\n      url\n      needPrescription\n      catalogID\n      isLeasing\n      isBlacklisted\n      menu {\n        id\n        name\n        url\n        __typename\n      }\n      category {\n        id\n        name\n        title\n        breadcrumbURL\n        isAdult\n        detail {\n          id\n          name\n          breadcrumbURL\n          isAdult\n          __typename\n        }\n        __typename\n      }\n      blacklistMessage {\n        title\n        description\n        button\n        url\n        __typename\n      }\n      txStats {\n        transactionSuccess\n        transactionReject\n        countSold\n        paymentVerified\n        itemSoldPaymentVerified\n        __typename\n      }\n      stats {\n        countView\n        countReview\n        countTalk\n        rating\n        __typename\n      }\n      __typename\n    }\n    components {\n      name\n      type\n      position\n      data {\n        ...ProductMedia\n        ...ProductHighlight\n        ...ProductInfo\n        ...ProductDetail\n        ...ProductSocial\n        ...ProductDataInfo\n        ...ProductCustomInfo\n        ...ProductVariant\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n"
                    }
                ]
            data = json.dumps(payload)

            headers = {
                'authority': 'gql.tokopedia.com',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
                'content-type': 'application/json',
                'accept': '*/*',
                'x-source': 'tokopedia-lite',
                'x-device': 'desktop',
                'x-tkpd-lite-service': 'zeus',
                'x-tkpd-akamai': 'pdpGetLayout',
                'sec-gpc': '1',
                'sec-fetch-site': 'same-site',
                'sec-fetch-mode': 'cors',
                'sec-fetch-dest': 'empty',
                'accept-language': 'en-US,en;q=0.9',
                # 'cookie': '_UUID_NONLOGIN_=f27a4fbb262751e7f59cedf8dc20b920; _UUID_NONLOGIN_.sig=Hp9ftFod1XGVPNEK3WDmqDWE5q0; DID=8f0b5ee08e63d5cb01508be397b525c65bcd51c937be8234c059aa99f503354617e297c8fc05e9f1fb2295013657811f; DID_JS=OGYwYjVlZTA4ZTYzZDVjYjAxNTA4YmUzOTdiNTI1YzY1YmNkNTFjOTM3YmU4MjM0YzA1OWFhOTlmNTAzMzU0NjE3ZTI5N2M4ZmMwNWU5ZjFmYjIyOTUwMTM2NTc4MTFm47DEQpj8HBSa+/TImW+5JCeuQeRkm5NMpJWZG3hSuFU=; bm_sz=F9145F22A84092AE45098162BE41E752~YAAQyxXfrQ6Bw299AQAANENQcw0lHAlP/a4QIoJU/lXcUsu6EHSuzGHjOM+PmG58gk10toRJx4msMpBA0tzo06HCHrIIa7atASFzlh+KHgPDWqak/++5RtNeO1CXqixDgC9CWrBsP4fYVJrkhFa5PJhQm7aSytbzMrHI7MFl+i1pQsDAV//YBO+rEOW/9SrsWKhAKwLsr0Vv1TvZSZIrtbE8DWnvTZUjjVE8+/nXV3NcRtd+RA8KBerOAGUV3V/oxs40Dd2gM/2ELaARDMFCMT73DRi4LgezL+K5KnDfSSsqI2qLMbQ=~3553590~3553605; ak_bmsc=2BBDE757975D4CF99A09EA1AD2C0DFC4~000000000000000000000000000000~YAAQyxXfrRKBw299AQAABUhQcw1GryNoOdTWDnzQ4l4lUsbLOHmnRHq1nQlFy853A4eflrcZ8GRNEQw0foAbbL/VHnDITJctNzyzJykPESU9NkZI50QO4fQsMQHKo88T3cu2woTfFA4wzOmhVD5CgX64/wmDMZ9akNSn9B2kZe5CGVrRglt1fdYmvUqszRvuTFWDiuRjR01qFEuM7c2cJsFfYOJzcvIZSp09VJgR0DeT46afu/mYgUWjj+dL3PtLSDutR2OV5omUuwwpBn0Br0Ctb1/LE7mnX3Q691gwQwoqK8BnaijqvW/4R7bjs1HFziwL4bmjxc+NAhP7UB23f1ZDkzLcxvdlYH4OuGZ2UpDcoTgC29MZrujJoOstfiBU0iUPlyArQZUP4n4=; _SID_Tokopedia_=6urEQcgCufTbcWGpI0cenOH09URIJ2UVPaSj5ZzekBjBjnIwbphisip2GWjHJqwIaNPigHfMloug2FQzdA7KPw8DViiglzNB6tXOyAr-6qI5DUG0nNBM25Ex06-mfb2G; bm_mi=D79F8510FAC49A3D10EDBAD68A5BB773~3KijlFBSRlacbn5kji77g0IhUjcVk5yzG4p3363nDAj+bjI5GsDJJjNS129U+Uca/ElkjQXFbrbxoqMoJawWslkyHz/G4GBK2w5+PZhFIzJhE1ISWHiMTykeWGnANtD15ipjyxDwFHbPqiimfMFhegFz/w5TSinlD6goC8hyI/ZODj8CSzvMg4Kstd0uZJ/fhd+7MPHdIy7gwM0qfGf7wbKkXA+fXaoOnj4ofMcmhNjtYHOEmPdsq+OlSZPBDk7Izk2a4pd2K9xQOISqp9D3h5e2ggu07FjN90mwAPZQzCUbd9VZT17DD2Ez8i04p8fl9U7lJUhym5baY4QK/q42AA==; bm_sv=3C1C919EF5958BA72D073627E7C76C64~CwDH6TXXmBNzH2A0W9m5ryAIzii7pZYUfiUkAEIBoWJmNtBtxzgLeu3WzmsredzMOZPBejM8VCmOR+zJyNT05ikK8QGZ7tXgiG8beB8DA3Xk1iDw1evp1XF0tiLeAXR/ULCBsc4XKXlzzv10MZgCZ+5u5asNqUwCzol2BsEqWRw=; _CAS_={"dId":2274,"aId":0,"lbl":"Jakarta Pusat","cId":176,"long":"","lat":"","pCo":"","wId":12210375,"sId":11530573}; _abck=0606DF49F4D1546D546D50EC3EA27A65~0~YAAQzRXfrSudsjJ9AQAAXh9bcwaY1aAc2sWbjUB7RlpY9ywwofQRkUqt0cSUQaC/7X6AUR3ailJJlxajA0q+DHX09B5kSB/+URG+wKZlg5prYD9JjvnLJNbETmirl0xa0RaoRN+eu2L5Y9TmA/U0mFJgO1+M8cpo38uD6bSMieVWzOKjvlr62Mz54gKlmBefqguV72suk0rOSZnGHaL6HWqm3a++q0iHhmv8aNpmfoB9ECz/3JW1PHtbdq/K2sM5VvbNEH9v3Dk6zA3zfrZDMjKIlHSz/lbVvy7DL/lDstk7fj8FwHs2YhsFqasq/yjbUW1BUSweSt1qvlTOU8keElGjcWZpYrb4buQsESvonNXxNEdzKCq8hq9GJc1Bx1xJ0yH8tV/+cziVZLEfCGH4FmEjiv/P/vPVTLbG~-1~-1~-1; hfv_banner=true',

                'cookie': cookies,
            }
            # while True:
                # try:
                #     proxy = getProxy()
                #     break
                # except:
                #     pass

            # proxies = {'https': 'https://'+proxy}
            res = requests.post('https://gql.tokopedia.com/', headers=headers, data=data, timeout=2)
            break
        except:
            pass'''

    shopDomain = item_description.split("/")[0]
    productKey = item_description.split("/")[1]
    products = json.loads(prods[1:-1])

    var_links = []
    try:
        for i in products['data']['pdpGetLayout']['components']:
            if i['name'] == 'variant_options':
                for u in i['data']:
                    for e in u:
                        if e == 'children':
                            for l in u[e]:
                                var_links.append(l['productURL'].split("/")[-1])
    except:
        pass

    checking_list = []
    for i in var_links:
        if i == productKey and len(var_links) > 1:
            for u in products['data']['pdpGetLayout']['components']:
                if u['name'] == "variant_options":
                    for nr, r in enumerate(u['data'][0]['variants']):
                        checking_list.append([])
                        for m in r['option']:
                            name = m['value']
                            checking_list[nr].append(name)


            new_checking_list = []
            for i in list(itertools.product(*checking_list)):
                new_checking_list.append(slugify(" ".join(i)))


            for i in new_checking_list:
                if productKey.endswith(i):
                    new_key = productKey[:-(len(i) + 1)]
                    return redirect('product_page_tokopedia', item_description=shopDomain + "/" + new_key)

    images = []
    videos = []
    models = []
    # models2 = []
    prices = []

    weight = int(str(products['data']['pdpGetLayout']['basicInfo']['weight']))/1000

    name = json.loads(products['data']['pdpGetLayout']['pdpSession'])['pn']

    rating = products['data']['pdpGetLayout']['basicInfo']['stats']['rating']

    shop_name = products['data']['pdpGetLayout']['basicInfo']['shopName']

    id = products['data']['pdpGetLayout']['basicInfo']['id']

    pdpSesion = products['data']['pdpGetLayout']['pdpSession']



    for i in products['data']['pdpGetLayout']['components']:
        if i['name'] == 'product_media':
            for u in i['data'][0]['media']:
                if u['type'] == 'image':
                    images.append(u['urlThumbnail'].replace("/200-square/", "/900/"))
                elif u['type'] == 'video':
                    videos.append(u['videoUrl'])
        if i['name'] == 'variant_options':
            for u in i['data']:
                for e in u:
                    if e == 'children':
                        for l in u[e]:
                            # models.append({'name': l['productName'].replace(name, "")[3:], 'price': convert_price(str(int(l['price']))), 'stock': l['stock']['stock']})
                            models.append({'name': l['productName'].replace(name, "")[3:], 'price': int(int(l['price']) + (int(l['price'])*0.1)), 'stock': l['stock']['stock']})
                            prices.append(int(int(l['price']) + (int(l['price'])*0.1)))



    for i in products['data']['pdpGetLayout']['components']:
        if i['name'] == 'product_detail':
            for u in i['data'][0]['content']:
                if u['title'] == "Deskripsi":
                    description = u['subtitle']
        if i['name'] == 'product_content':
            rezerv_price = int(int(i['data'][0]['price']['value']) + (int(i['data'][0]['price']['value'])*0.1))


    prices.sort()
    try:
        price_min = prices[0]
        price_max = prices[-1]
    except:
        prices.append(rezerv_price)
        price_min = prices[0]
        price_max = prices[-1]

    if models == []:
        # models.append({'name': "", 'price': convert_price(str(int(rezerv_price))), 'stock': 99})
        models.append({'name': "", 'price': rezerv_price, 'stock': 99})

    ####################################################################################################################

    headers = {
        'authority': 'gql.tokopedia.com',
        'sec-ch-ua': '^\\^Chromium^\\^;v=^\\^92^\\^, ^\\^',
        'x-version': '27ca28b',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
        'content-type': 'application/json',
        'accept': '*/*',
        'x-source': 'tokopedia-lite',
        'x-device': 'desktop',
        'x-tkpd-lite-service': 'zeus',
        'x-tkpd-akamai': 'pdpGetData',
        'origin': 'https://www.tokopedia.com',
        'sec-fetch-site': 'same-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': f'https://www.tokopedia.com/{item_description}'.encode('unicode_escape').decode("utf-8"),
        'accept-language': 'en-US,en;q=0.9',
    }

    data = [
        {
            "operationName": "PDPGetDataP2",
            "variables": {
                "productID": f"{id}",
                "pdpSession": pdpSesion,
                "deviceID": "",
                "userLocation": {
                    "addressID": "0",
                    "districtID": "2166",
                    "postalCode": "",
                    "latlon": ""
                },
                "affiliate": {
                    "uuid": "",
                    "trackerID": "",
                    "irisSessionID": ""
                }
            },
            "query": "query PDPGetDataP2($productID: String!, $pdpSession: String!, $deviceID: String, $userLocation: pdpUserLocation, $affiliate: pdpAffiliate) {\n  pdpGetData(productID: $productID, pdpSession: $pdpSession, deviceID: $deviceID, userLocation: $userLocation, affiliate: $affiliate) {\n    error {\n      Code\n      Message\n      DevMessage\n      __typename\n    }\n    callsError {\n      shopInfo {\n        Code\n        Message\n        __typename\n      }\n      cartRedirection {\n        Code\n        Message\n        __typename\n      }\n      nearestWarehouse {\n        Code\n        Message\n        __typename\n      }\n      __typename\n    }\n    productView\n    wishlistCount\n    shopInfo {\n      shopTier\n      badgeURL\n      closedInfo {\n        closedNote\n        reason\n        detail {\n          openDate\n          __typename\n        }\n        __typename\n      }\n      isOpen\n      favoriteData {\n        totalFavorite\n        alreadyFavorited\n        __typename\n      }\n      activeProduct\n      createInfo {\n        epochShopCreated\n        __typename\n      }\n      shopAssets {\n        avatar\n        __typename\n      }\n      shopCore {\n        domain\n        shopID\n        name\n        shopScore\n        url\n        __typename\n      }\n      shopLastActive\n      location\n      statusInfo {\n        shopStatus\n        isIdle\n        __typename\n      }\n      isAllowManage\n      isOwner\n      isCOD\n      shopType\n      __typename\n    }\n    merchantVoucher {\n      vouchers {\n        voucher_id\n        voucher_name\n        voucher_type {\n          voucher_type\n          identifier\n          __typename\n        }\n        voucher_code\n        amount {\n          amount\n          amount_type\n          amount_formatted\n          __typename\n        }\n        minimum_spend\n        valid_thru\n        tnc\n        banner {\n          desktop_url\n          mobile_url\n          __typename\n        }\n        status {\n          status\n          identifier\n          __typename\n        }\n        in_use_expiry\n        __typename\n      }\n      __typename\n    }\n    nearestWarehouse {\n      product_id\n      stock\n      stock_wording\n      price\n      warehouse_info {\n        warehouse_id\n        is_fulfillment\n        district_id\n        postal_code\n        geolocation\n        __typename\n      }\n      __typename\n    }\n    installmentRecommendation {\n      message\n      data {\n        term\n        mdr_value\n        mdr_type\n        interest_rate\n        minimum_amount\n        maximum_amount\n        monthly_price\n        os_monthly_price\n        partner_code\n        partner_name\n        partner_icon\n        __typename\n      }\n      __typename\n    }\n    productWishlistQuery {\n      value\n      __typename\n    }\n    cartRedirection {\n      status\n      error_message\n      data {\n        product_id\n        config_name\n        hide_floating_button\n        available_buttons {\n          text\n          color\n          cart_type\n          onboarding_message\n          show_recommendation\n          __typename\n        }\n        unavailable_buttons\n        __typename\n      }\n      __typename\n    }\n    shopTopChatSpeed {\n      messageResponseTime\n      __typename\n    }\n    shopRatingsQuery {\n      ratingScore\n      __typename\n    }\n    shopPackSpeed {\n      speedFmt\n      hour\n      __typename\n    }\n    shopFeature {\n      IsGoApotik\n      __typename\n    }\n    ratesEstimate {\n      warehouseID\n      products\n      data {\n        destination\n        title\n        subtitle\n        courierLabel\n        eTAText\n        title\n        errors {\n          code: Code\n          message: Message\n          devMessage: DevMessage\n          __typename\n        }\n        __typename\n      }\n      bottomsheet {\n        title\n        iconURL\n        subtitle\n        buttonCopy\n        __typename\n      }\n      __typename\n    }\n    restrictionInfo {\n      message\n      restrictionData {\n        productID\n        isEligible\n        action {\n          actionType\n          title\n          description\n          attributeName\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n"
        }
    ]

    response = requests.post('https://gql.tokopedia.com/', headers=headers, json=data)
    t = json.loads(response.text)

    district_id = t[0]['data']['pdpGetData']['nearestWarehouse'][0]['warehouse_info']['district_id']
    post_code = t[0]['data']['pdpGetData']['nearestWarehouse'][0]['warehouse_info']['postal_code']
    geolocation = t[0]['data']['pdpGetData']['nearestWarehouse'][0]['warehouse_info']['geolocation']



    ####################################################################################################################


    headers = {
        'authority': 'gql.tokopedia.com',
        'sec-ch-ua': '^\\^Chromium^\\^;v=^\\^92^\\^, ^\\^',
        'x-version': '27ca28b',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
        'content-type': 'application/json',
        'accept': '*/*',
        'x-source': 'tokopedia-lite',
        'x-tkpd-lite-service': 'zeus',
        'origin': 'https://www.tokopedia.com',
        'sec-fetch-site': 'same-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': f'https://www.tokopedia.com/{item_description}'.encode('unicode_escape').decode("utf-8"),
        'accept-language': 'en-US,en;q=0.9',
    }

    data = [
        {
            "operationName": "ratesEstimateQuery",
            "variables": {
                "weight": weight,
                "domain": f"{item_description}".split("/")[0],
                "productId": f"{id}",
                "origin": district_id + "|" + post_code + "|" + geolocation,
                "destination": "2166||",
                "POTime": 0,
                "isFulfillment": False,
                "deviceType": "default_v3",
                "shopTier": 2
            },
            "query": "query ratesEstimateQuery($weight: Float!, $domain: String!, $origin: String, $productId: String, $destination: String, $POTime: Int, $isFulfillment: Boolean, $deviceType: String, $shopTier: Int) {\n  ratesEstimateV3(input: {weight: $weight, domain: $domain, origin: $origin, product_id: $productId, destination: $destination, po_time: $POTime, type: $deviceType, is_fulfillment: $isFulfillment, shop_tier: $shopTier}) {\n    data {\n      address {\n        city_name\n        province_name\n        district_name\n        country\n        postal_code\n        address\n        lat\n        long\n        phone\n        addr_name\n        address_1\n        receiver_name\n        __typename\n      }\n      shop {\n        district_id\n        district_name\n        postal_code\n        origin\n        addr_street\n        latitude\n        longitude\n        province_id\n        city_id\n        city_name\n        __typename\n      }\n      rates {\n        id\n        rates_id\n        type\n        services {\n          service_name\n          service_id\n          service_order\n          status\n          range_price {\n            min_price\n            max_price\n            __typename\n          }\n          texts {\n            text_service_desc\n            text_service_notes\n            text_range_price\n            text_etd\n            text_price\n            __typename\n          }\n          products {\n            shipper_name\n            shipper_id\n            shipper_product_id\n            shipper_product_name\n            shipper_weight\n            price {\n              price\n              formatted_price\n              __typename\n            }\n            texts {\n              text_etd\n              text_range_price\n              text_eta_summarize\n              __typename\n            }\n            cod {\n              is_cod_available\n              __typename\n            }\n            eta {\n              text_eta\n              error_code\n              __typename\n            }\n            features {\n              dynamic_price {\n                text_label\n                __typename\n              }\n              __typename\n            }\n            __typename\n          }\n          cod {\n            is_cod\n            cod_text\n            __typename\n          }\n          order_priority {\n            is_now\n            __typename\n          }\n          etd {\n            min_etd\n            max_etd\n            __typename\n          }\n          range_price {\n            min_price\n            max_price\n            __typename\n          }\n          __typename\n        }\n        __typename\n      }\n      texts {\n        text_min_price\n        text_destination\n        text_eta\n        __typename\n      }\n      is_blackbox\n      __typename\n    }\n    __typename\n  }\n}\n"
        }
    ]

    response = requests.post('https://gql.tokopedia.com/', headers=headers, json=data)

    prov_list = []
    for i in json.loads(response.text)[0]['data']['ratesEstimateV3']['data']['rates']['services']:
        for u in i['products']:

            if "Instant" in u['shipper_product_name'] or "Same Day" in u['shipper_product_name']:
                continue
            prov_list.append(u['shipper_name'])

    ship = ""
    if "JNE Reg" in prov_list:
        ship = "JNE Reg"
    else:
        for i in prov_list:
            if "JNE" in i:
                ship = i
                break
    if ship == "":
        for i in prov_list:
            if "JNT" in i or "TIKI" in i:
                ship = i
                break

    if ship == "":
        for i in prov_list:
            if "SiCepat" in i or "Wahana" in i:
                continue
            else:
                ship = i

    if ship == "":
        try:
            ship = prov_list[0]
        except:
            pass



    if ship != "":
        for i in json.loads(response.text)[0]['data']['ratesEstimateV3']['data']['rates']['services']:
            for u in i['products']:
                if u['shipper_name'] == ship:
                    shipping_price = int(int(u['price']['price']) + (int(u['price']['price']) *0.1))


    context_product_tokopedia = {
                                                 "id": productKey,
                                                 "url": "https://www.tokopedia.com/"+item_description,
                                                 "name": name,
                                                 "images": images,
                                                 "image": images[0],
                                                 "videos": videos,
                                                 "item_rating": rating,
                                                 "price_min": price_min,
                                                 "price_max": price_max,
                                                 "description": description,
                                                 "models": models,
                                                 "shop_location": shop_name,
                                                 "shipping": shipping_price,
                                                 }


    try:
        product_obj = product_view.objects.create(
            id = productKey,
            name = name,
            url = item_description,
            price_min = price_min,
            price_max = price_max,
            shipping = shipping_price,
            models = json.dumps(models),
        )
        product_obj.save()
    except:
        product_view.objects.filter(id=productKey).delete()
        product_obj = product_view.objects.create(
            id = productKey,
            name = name,
            url = item_description,
            price_min = price_min,
            price_max = price_max,
            shipping = shipping_price,
            models = json.dumps(models),
        )
        product_obj.save()

    return render(request, 'product_page.html', context_product_tokopedia)


@login_required(login_url=login_page)
def my_orders(request):
    if request.method == 'POST':
        form = refundForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(my_orders)
    else:

        def convert_price(price1):
            price_1 = price1[::-1]
            price_2 = ''
            while price_1:
                price_2 += price_1[:3]
                if len(price_1) > 3:
                    price_2 += ','
                price_1 = price_1[3:]
            return price_2[::-1]
        context = {}
        context['orders'] = {}
        items_ship = shipping.objects.all().filter(client_email=request.user.email)
        statuses = {}
        for i in items_ship:
            ids = json.loads(i.sold_ids)
            for id in ids:
                statuses[id] = i.shipping_status
        items = sold.objects.all().filter(client_email=request.user.email)
        for item in items:
            try:
                shipping_status = statuses[str(item.id)]
            except:
                shipping_status = "NOT PAID"
            if item.order_status == "CANCELLED":
                can_ship = "False"
            elif item.height == 0.0 and item.length == 0.0 and item.width == 0.0 and item.width == 0.0:
                can_ship = "False"
            else:
                if shipping_status == "NOT PAID":
                    can_ship = "True"
                else:
                    can_ship = "False"

            context['orders'][item.id] = {
                "id":item.id,
                "name":item.name,
                "variant":item.variant,
                "price": convert_price(str(int(item.price))),
                "rmprice": item.rmprice,
                "url":item.url,
                "quantity":item.quantity,
                "shipping_status": shipping_status,
                "order_status": item.order_status,
                "extra_info": item.extra_info,
                "can_ship": can_ship,

            }

        context['cart'] = {}
        items = cart.objects.all().filter(client_email=request.user.email)
        for item in items:
            context['cart'][item.id] = {
                "id": item.id,
                "name": item.name,
                "variant": item.variant,
                "price": convert_price(str(int(item.price))),
                "rmprice": item.rmprice,
                "url": item.url,
                "quantity": item.quantity,
            }



        context['new_bills'] = {}
        items = new_bills.objects.all().filter(client_email=request.user.email, bill_status="NOT PAID")
        for item in items:
            context['new_bills'][item.id] = {
                "email": item.client_email,
                "bill_code": item.bill_code,
                "description": item.description,
                "price": item.price,
            }

        item = wallet.objects.all().filter(client_email=request.user.email)[0]
        context['balance'] = item.balance


        hist = history.objects.all().filter(client_email=request.user.email)
        context['history'] = hist

        refund_form = refundForm()
        refund_form.fields["client_email"].initial = request.user.email
        context['refund_form'] = refund_form
        return render(request, 'my_orders.html', context)


@login_required(login_url=login_page)
def addCart_shopee(request, item_id, variant, quantity):
    items = product_view.objects.all().filter(id=item_id)
    price = ""
    for i in json.loads(items[0].models):
        if variant == i['name']:
            price = i['price']
            break
    if variant == "Default" and price == "":
        price = json.loads(items[0].models)[0]['price']

    str_id = str(request.user.id)
    while len(str_id) < 6:
        str_id = "0"+str_id


    # bill_desc = items[0].name + " " + variant
    # data = {
    # 'userSecretKey' : 'lctchung-fg0p-uubc-qlpt-iqg51fc1954s',
    # 'categoryCode' : '6elrtbk8',
    # 'billName' : 'Purchase from Tolongbeli',
    # 'billDescription' : bill_desc[:99],
    # 'billPriceSetting' : 1,
    # 'billPayorInfo' : 0,
    # 'billAmount' : round((int(price*quantity + items[0].shipping)/3300)*100, 2),
    # 'billReturnUrl' : 'http://127.0.0.1:8000/',
    # 'billCallbackUrl' : 'http://127.0.0.1:8000/',
    # 'billExternalReferenceNo' : "MY"+str_id,
    # 'billTo' : request.user.username,
    # 'billEmail' : request.user.email,
    # 'billPhone' : "",
    # 'billSplitPayment' : 0,
    # 'billSplitPaymentArgs' : '',
    # 'billPaymentChannel' : '0',
    # 'billContentEmail' : 'Thank you for purchasing our product!',
    # 'billChargeToCustomer' : 2,
    # }
    # req = requests.post('https://toyyibpay.com/index.php/api/createBill', data=data)
    #
    # bill_code = json.loads(req.text)[0]['BillCode']
    product_buy = cart.objects.create(
        id_product = items[0].id,
        name = items[0].name,
        price = int(price*quantity + items[0].shipping),
        rmprice= round(int(price*quantity + items[0].shipping)/3300, 2),
        variant = variant,
        url = "/shopee/"+items[0].url,
        client_email=request.user.email,
        client_id="MY"+str_id,
        quantity=quantity,
    )

    product_buy.save()
    # return HttpResponseRedirect(f"https://toyyibpay.com/{bill_code}")

    return redirect(my_orders)


@login_required(login_url=login_page)
def addCart_tokopedia(request, item_id, variant, quantity):


    items = product_view.objects.all().filter(id=item_id)
    price = ""
    for i in json.loads(items[0].models):
        if variant == i['name']:
            price = i['price']
            break
    if variant == "Default" and price == "":
        price = json.loads(items[0].models)[0]['price']

    str_id = str(request.user.id)
    while len(str_id) < 6:
        str_id = "0"+str_id


    product_buy = cart.objects.create(
        id_product = items[0].id,
        name = items[0].name,
        price = int(price*quantity + items[0].shipping),
        rmprice= round(int(price*quantity + items[0].shipping)/3300, 2),
        variant = variant,
        url = "/tokopedia/"+items[0].url,
        client_email=request.user.email,
        client_id="MY"+str_id,
        quantity=quantity,
    )

    product_buy.save()
    # return HttpResponseRedirect(f"https://toyyibpay.com/{bill_code}")

    return redirect(my_orders)


@csrf_exempt
def buy(request):

    if request.method == "POST":
        dict = json.loads(request.POST.get("Products"))

        price = 0
        ids = []
        for id in dict:
            product = cart.objects.all().filter(client_email=request.user.email, id=id)[0]
            product.extra_info = dict[id]
            product.save()

            item = cart.objects.all().filter(client_email=request.user.email, id=id)[0]
            price += item.rmprice
            ids.append(id)

        str_id = str(request.user.id)
        while len(str_id) < 6:
            str_id = "0" + str_id







        item = wallet.objects.all().filter(client_email=request.user.email)[0]
        balance = item.balance

        if balance >= price:

            item.balance = round(balance - price, 2)
            item.save()
            for id in ids:
                bill = order_bills.objects.create(
                    cart_id=id,
                    bill_code="balance",
                    client_email=request.user.email,
                    client_id=str_id,
                )

                bill.save()
            return JsonResponse(status=302, data={'success': f"/my_orders"})
        elif balance != 0:

            new_price = round(price - balance, 2)

            data = {
            'userSecretKey' : 'lctchung-fg0p-uubc-qlpt-iqg51fc1954s',
            'categoryCode' : '6elrtbk8',
            'billName' : 'Purchase from Tolongbeli',
            'billDescription' : "Paying for your product(s)",
            'billPriceSetting' : 1,
            'billPayorInfo' : 0,
            'billAmount' : new_price*100,
            'billReturnUrl' : 'http://103.171.26.128:8001/my_orders',
            'billCallbackUrl' : 'http://103.171.26.128:8001/my_orders',
            'billExternalReferenceNo' : "MY"+str_id,
            'billTo' : request.user.username,
            'billEmail' : request.user.email,
            'billPhone' : "",
            'billSplitPayment' : 0,
            'billSplitPaymentArgs' : '',
            'billPaymentChannel' : '0',
            'billContentEmail' : 'Thank you for purchasing our product(s)!',
            'billChargeToCustomer' : 2,
            }
            req = requests.post('https://toyyibpay.com/index.php/api/createBill', data=data)

            bill_code = json.loads(req.text)[0]['BillCode']

            for id in ids:

                bill = order_bills.objects.create(
                    cart_id = id,
                    bill_code = bill_code,
                    client_email=request.user.email,
                    client_id=str_id,
                    notes=f"Total was {price} - {balance} paid from balance;"
                )

                bill.save()

                item.balance = 0
                item.save()

            return JsonResponse(status = 302 , data = {'success' : f"https://toyyibpay.com/{bill_code}" })


        else:

            data = {
            'userSecretKey' : 'lctchung-fg0p-uubc-qlpt-iqg51fc1954s',
            'categoryCode' : '6elrtbk8',
            'billName' : 'Purchase from Tolongbeli',
            'billDescription' : "Paying for your product(s)",
            'billPriceSetting' : 1,
            'billPayorInfo' : 0,
            'billAmount' : price*100,
            'billReturnUrl' : 'http://103.171.26.128:8001/my_orders',
            'billCallbackUrl' : 'http://103.171.26.128:8001/my_orders',
            'billExternalReferenceNo' : "MY"+str_id,
            'billTo' : request.user.username,
            'billEmail' : request.user.email,
            'billPhone' : "",
            'billSplitPayment' : 0,
            'billSplitPaymentArgs' : '',
            'billPaymentChannel' : '0',
            'billContentEmail' : 'Thank you for purchasing our product(s)!',
            'billChargeToCustomer' : 2,
            }
            req = requests.post('https://toyyibpay.com/index.php/api/createBill', data=data)

            bill_code = json.loads(req.text)[0]['BillCode']

            for id in ids:

                bill = order_bills.objects.create(
                    cart_id = id,
                    bill_code = bill_code,
                    client_email=request.user.email,
                    client_id=str_id,
                )

                bill.save()
            return JsonResponse(status = 302 , data = {'success' : f"https://toyyibpay.com/{bill_code}" })


    # product_buy = sold.objects.create(
    #     id_product = items[0].id,
    #     name = items[0].name,
    #     price = int(price*quantity + items[0].shipping),
    #     rmprice= round(int(price*quantity + items[0].shipping)/3300, 2),
    #     variant = variant,
    #     url = "/shopee/"+items[0].url,
    #     client_email=request.user.email,
    #     client_id="MY"+str_id,
    #     quantity=quantity,
    #     shipping_rate=rate,
    #     shipping_country=country,
    # )


def removeCart(request, item_id):

    cart.objects.get(id=item_id).delete()
    return redirect(my_orders)


def calculator(request):
    if request.method == "POST":

        configurations = calc_conf.objects.all()[0]
        markup = configurations.markup/100
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
        country = request.POST.get("country")

        if country == "malaysia1":
            normal = malaysia1_rate
            sensitive = malaysia1_sensitive_rate
        elif country == "malaysia2":
            normal = malaysia2_rate
            sensitive = malaysia2_sensitive_rate
        elif country == "singapore":
            normal = singapore_rate
            sensitive = singapore_sensitive_rate
        elif country == "brunel":
            normal = brunel_rate
            sensitive = brunel_sensitive_rate


        item_price = request.POST.get("item_price")
        try:
            float(item_price)
        except:
            item_price = 0

        domestic = request.POST.get("domestic")
        try:
            float(domestic)
        except:
            domestic = 0

        cost = round(round((int(item_price)+int(domestic))/convert_rate, 1) + (int(item_price)+int(domestic))/convert_rate*markup, 2)
        context = {}
        context['item_price'] = cost

        #################### AIR SHIPPING


        rate = request.POST.get("rate")
        length = request.POST.get("length")
        width = request.POST.get("width")
        height = request.POST.get("height")
        weight = request.POST.get("weight")
        w1 = math.ceil(float(length)*float(width)*float(height)/air_number)
        w2 = math.ceil(float(weight))
        if rate == "normal":
            rm = normal
        elif rate == "sensitive":
            rm = sensitive
        if w1 > w2:
            air_price = w1*rm+(w1*rm*markup)
            total_air_price = (w1*rm+(w1*rm*markup))+cost
        else:
            air_price = w2*rm+(w2*rm*markup)
            total_air_price = (w2*rm+(w2*rm*markup))+cost

        context['air_price'] = round(air_price, 2)
        context['total_air_price'] = round(total_air_price, 2)



        #################### SEA SHIPPING


        w1 = math.ceil(float(length)*float(width)*float(height)/sea_1_number)/10
        if w1 < sea_1_min:
            w1 = sea_1_min


        w2 = math.ceil(float(weight))
        cbm = math.ceil(w2/40)/10
        if cbm < sea_1_min:
            cbm = sea_1_min

        if w1 > cbm:
            sea_price = (w1 - sea_1_min)*sea_1_price_over_min + sea_1_price_under_min
            total_sea_price = ((w1 - sea_1_min)*sea_1_price_over_min + sea_1_price_under_min)+cost
        else:
            sea_price = (cbm - sea_1_min)*sea_1_price_over_min + sea_1_price_under_min
            total_sea_price = ((cbm - sea_1_min)*sea_1_price_over_min + sea_1_price_under_min)+cost

        context['sea_price'] = round(sea_price, 2)
        context['total_sea_price'] = round(total_sea_price, 2)


        #################### SEA 2 SHIPPING

        w1 = math.ceil(float(length)*float(width)*float(height)/sea_2_number)
        w2 = math.ceil(float(weight))
        if w1 < sea_2_min:
            w1 = sea_2_min
        if w2 < sea_2_min:
            w2 = sea_2_min
        if w1 > w2:
            sea2_price = (w1 - sea_2_min)*sea_2_price_over_min + sea_2_price_under_min
            total_sea2_price = ((w1 - sea_2_min)*sea_2_price_over_min + sea_2_price_under_min)+cost
        else:
            sea2_price = (w2 - sea_2_min)*sea_2_price_over_min + sea_2_price_under_min
            total_sea2_price = ((w2 - sea_2_min)*sea_2_price_over_min + sea_2_price_under_min)+cost

        context['sea2_price'] = round(sea2_price, 2)
        context['total_sea2_price'] = round(total_sea2_price, 2)


        return render(request, 'calculator.html', context)
    else:
        #
        # conf_obj = calc_conf.objects.create(
        #     markup = 10,
        #     singapore_rate = 35,
        #     singapore_sensitive_rate = 40,
        #     brunel_rate = 35,
        #     brunel_sensitive_rate =  40,
        #     malaysia1_rate = 35,
        #     malaysia1_sensitive_rate =  40,
        #     malaysia2_rate = 35,
        #     malaysia2_sensitive_rate =  40,
        #     convert_rate = 3300,
        #     air_number = 5000,
        #     sea_1_number = 100000,
        #     sea_2_number = 5000,
        #     sea_1_min = 0.3,
        #     sea_1_price_under_min = 220,
        #     sea_1_price_over_min = 550,
        #     sea_2_min = 10,
        #     sea_2_price_under_min = 80,
        #     sea_2_price_over_min = 10,
        # )
        # conf_obj.save()

        return render(request, 'calculator.html', {})


def check_admin(user):
   return user.is_superuser


@user_passes_test(check_admin)
def calculator_config(request):
    if request.method == "POST":
        configurations = calc_conf.objects.all()[0]
        configurations.markup = request.POST.get("markup")
        configurations.singapore_rate = request.POST.get("singapore_rate")
        configurations.singapore_sensitive_rate = request.POST.get("singapore_sensitive_rate")
        configurations.brunel_rate = request.POST.get("brunel_rate")
        configurations.brunel_sensitive_rate = request.POST.get("brunel_sensitive_rate")
        configurations.malaysia1_rate = request.POST.get("malaysia1_rate")
        configurations.malaysia1_sensitive_rate = request.POST.get("malaysia1_sensitive_rate")
        configurations.malaysia2_rate = request.POST.get("malaysia2_rate")
        configurations.malaysia2_sensitive_rate = request.POST.get("malaysia2_sensitive_rate")
        configurations.convert_rate = request.POST.get("convert_rate")
        configurations.air_number = request.POST.get("air_number")
        configurations.sea_1_number = request.POST.get("sea_1_number")
        configurations.sea_2_number = request.POST.get("sea_2_number")
        configurations.sea_1_min = request.POST.get("sea_1_min")
        configurations.sea_1_price_under_min = request.POST.get("sea_1_price_under_min")
        configurations.sea_1_price_over_min = request.POST.get("sea_1_price_over_min")
        configurations.sea_2_min = request.POST.get("sea_2_min")
        configurations.sea_2_price_under_min = request.POST.get("sea_2_price_under_min")
        configurations.sea_2_price_over_min = request.POST.get("sea_2_price_over_min")
        configurations.save()
        return redirect(calculator_config)
    else:
        configurations = calc_conf.objects.all()[0]
        context = {}
        context['markup'] = configurations.markup
        context['singapore_rate'] = configurations.singapore_rate
        context['singapore_sensitive_rate'] = configurations.singapore_sensitive_rate
        context['brunel_rate'] = configurations.brunel_rate
        context['brunel_sensitive_rate'] = configurations.brunel_sensitive_rate
        context['malaysia1_rate'] = configurations.malaysia1_rate
        context['malaysia1_sensitive_rate'] = configurations.malaysia1_sensitive_rate
        context['malaysia2_rate'] = configurations.malaysia2_rate
        context['malaysia2_sensitive_rate'] = configurations.malaysia2_sensitive_rate
        context['convert_rate'] = configurations.convert_rate
        context['air_number'] = configurations.air_number
        context['sea_1_number'] = configurations.sea_1_number
        context['sea_2_number'] = configurations.sea_2_number
        context['sea_1_min'] = configurations.sea_1_min
        context['sea_1_price_under_min'] = configurations.sea_1_price_under_min
        context['sea_1_price_over_min'] = configurations.sea_1_price_over_min
        context['sea_2_min'] = configurations.sea_2_min
        context['sea_2_price_under_min'] = configurations.sea_2_price_under_min
        context['sea_2_price_over_min'] = configurations.sea_2_price_over_min



        return render(request, 'calculator_config.html', context)


@user_passes_test(check_admin)
def change_bill(request):
    if request.method == "POST":
        new_price = request.POST.get("price")
        email = request.POST.get("email")
        description = request.POST.get("description")

        str_id = str(request.user.id)
        while len(str_id) < 6:
            str_id = "0" + str_id

        data = {
            'userSecretKey': 'lctchung-fg0p-uubc-qlpt-iqg51fc1954s',
            'categoryCode': '6elrtbk8',
            'billName': 'Extra bill from Tolongbeli',
            'billDescription': description,
            'billPriceSetting': 1,
            'billPayorInfo': 0,
            'billAmount': float(new_price)*100,
            'billReturnUrl' : 'http://103.171.26.128:8001/my_orders',
            'billCallbackUrl' : 'http://103.171.26.128:8001/my_orders',
            'billExternalReferenceNo': "MY" + str_id,
            'billTo': email,
            'billEmail': email,
            'billPhone': "",
            'billSplitPayment': 0,
            'billSplitPaymentArgs': '',
            'billPaymentChannel': '0',
            'billContentEmail': 'Thank you for purchasing our product!',
            'billChargeToCustomer': 2,
        }
        req = requests.post('https://toyyibpay.com/index.php/api/createBill', data=data)

        bill_code = json.loads(req.text)[0]['BillCode']
        bill = new_bills.objects.create(
            bill_code=bill_code,
            description=description,
            client_email=request.user.email,
            price=new_price,
        )

        bill.save()
        return redirect(home)
    else:
        return render(request, 'change_bill.html', {})


@csrf_exempt
@login_required(login_url=login_page)
def pay_shipping(request):

    if request.method == "POST":
        dict = json.loads(request.POST.get("Products"))
        ids = dict['ids']
        prices = dict['prices']
        shippingi = dict['shipping']
        rate = dict['rate']
        country = dict['country']
        name = dict['name']
        address = dict['address']
        phone = dict['phone']
        postcode = dict['postcode']
        print(country)
        print(shippingi)
        allowed_shippment = allow_shipping.objects.all()[0]
        if shippingi == "air":
            if country == "Malaysia1" and allow_shipping.air_west_malaysia == 0:
                    return JsonResponse(status=404, data={'error': f"West Malaysia can't use air shipping!"})
            if country == "Malaysia2" and allow_shipping.air_east_malaysia == 0:
                    return JsonResponse(status=404, data={'error': f"East Malaysia can't use air shipping!"})
            if country == "Singapore" and allow_shipping.air_singapore == 0:
                    return JsonResponse(status=404, data={'error': f"Singapore can't use air shipping!"})
            if country == "Brunel" and allow_shipping.air_brunei == 0:
                    return JsonResponse(status=404, data={'error': f"Brunel can't use air shipping!"})
        if shippingi == "sea1":
            if country == "Malaysia1" and allow_shipping.sea_bulky_west_malaysia == 0:
                    return JsonResponse(status=404, data={'error': f"West Malaysia can't use this sea shipping!"})
            if country == "Malaysia2" and allow_shipping.sea_bulky_east_malaysia == 0:
                    return JsonResponse(status=404, data={'error': f"East Malaysia can't use sea shipping!"})
            if country == "Singapore" and allow_shipping.sea_bulky_singapore == 0:
                    return JsonResponse(status=404, data={'error': f"Singapore can't use sea shipping!"})
            if country == "Brunel" and allow_shipping.sea_bulky_brunei == 0:
                    return JsonResponse(status=404, data={'error': f"Brunel can't use sea shipping!"})
        if shippingi == "sea2":
            if country == "Malaysia1" and allow_shipping.sea_small_west_malaysia == 0:
                    return JsonResponse(status=404, data={'error': f"West Malaysia can't use sea shipping!"})
            if country == "Malaysia2" and allow_shipping.sea_small_east_malaysia == 0:
                    return JsonResponse(status=404, data={'error': f"East Malaysia can't use sea shipping!"})
            if country == "Singapore" and allow_shipping.sea_small_singapore == 0:
                    return JsonResponse(status=404, data={'error': f"Singapore can't use sea shipping!"})
            if country == "Brunel" and allow_shipping.sea_small_brunei == 0:
                    return JsonResponse(status=404, data={'error': f"Brunel can't use sea shipping!"})




        if shippingi == "air":
            price = prices['air']
            shipping_choose = "Air"
        if shippingi == "sea1":
            price = prices['sea1']
            shipping_choose = "Sea 1"
        if shippingi == "sea2":
            price = prices['sea2']
            shipping_choose = "Sea 2"

        for id in ids:
            item = sold.objects.all().filter(id=id, client_email=request.user.email)[0]
            if shippingi == "air":
                if item.allow_air == False:
                    return JsonResponse(status=404, data={'error': f"Product {id} can't be shipped with {shipping}"})
            if shippingi == "sea1":
                if item.allow_sea_1 == False:
                    return JsonResponse(status=404, data={'error': f"Product {id} can't be shipped with {shipping}"})
            if shippingi == "sea2":
                if item.allow_sea_2 == False:
                    return JsonResponse(status=404, data={'error': f"Product {id} can't be shipped with {shipping}"})


        str_id = str(request.user.id)
        while len(str_id) < 6:
            str_id = "0"+str_id

        item = wallet.objects.all().filter(client_email=request.user.email)[0]
        balance = item.balance

        if balance >= price:
            item.balance = round(balance - price, 2)
            item.save()

            bill = shipping_bills.objects.create(
                product_ids=json.dumps(ids),
                bill_code="balance",
                client_email=request.user.email,
                client_id=str_id,
                notes=f"Total was {price} - {price} paid from balance;"
            )
            bill.save()



            shipping_product = shipping.objects.create(
                sold_ids = json.dumps(ids),
                shipping_price = price,
                client_email=request.user.email,
                client_id=str_id,
                shipping_choose = shipping_choose,
                shipping_rate= rate,
                shipping_country= country,
                address= address,
                name= name,
                phone= phone,
                postcode= postcode,
            )
            shipping_product.save()

            # item = sold.objects.all().filter(id=id, client_email=request.user.email)[0]
            # item.shipping_price = data1[id]
            # if shipping == "air":
            #     item.shipping_choose = "Air"
            # if shipping == "sea1":
            #     item.shipping_choose = "Sea 1"
            # if shipping == "sea2":
            #     item.shipping_choose = "Sea 2"
            # item.shipping_rate = rate
            # item.shipping_country = country
            # item.save()
            return JsonResponse(status = 302 , data = {'success' : f"/my_orders" })
        elif balance != 0:
            new_price = round(price - balance, 2)
            data = {
            'userSecretKey' : 'lctchung-fg0p-uubc-qlpt-iqg51fc1954s',
            'categoryCode' : '6elrtbk8',
            'billName' : 'Purchase from Tolongbeli',
            'billDescription' : "Shipping fee for product(s) "+ ", ".join(ids),
            'billPriceSetting' : 1,
            'billPayorInfo' : 0,
            'billAmount' : new_price*100,
            'billReturnUrl' : 'http://103.171.26.128:8001/my_orders',
            'billCallbackUrl' : 'http://103.171.26.128:8001/my_orders',
            'billExternalReferenceNo' : "MY"+str_id,
            'billTo' : request.user.username,
            'billEmail' : request.user.email,
            'billPhone' : "",
            'billSplitPayment' : 0,
            'billSplitPaymentArgs' : '',
            'billPaymentChannel' : '0',
            'billContentEmail' : 'Thank you for purchasing our product!',
            'billChargeToCustomer' : 2,
            }
            req = requests.post('https://toyyibpay.com/index.php/api/createBill', data=data)

            bill_code = json.loads(req.text)[0]['BillCode']




            bill = shipping_bills.objects.create(
                product_ids = json.dumps(ids),
                bill_code = bill_code,
                client_email=request.user.email,
                client_id=str_id,
                notes=f"Total was {price} - {balance} paid from balance;"
            )
            bill.save()

            item.balance = 0
            item.save()


            shipping_product = shipping.objects.create(
                sold_ids = json.dumps(ids),
                shipping_price = price,
                client_email=request.user.email,
                client_id=str_id,
                shipping_choose = shipping_choose,
                shipping_rate= rate,
                shipping_country= country,
                address= address,
                phone= phone,
                name= name,
                postcode= postcode,
            )
            shipping_product.save()

                # item = sold.objects.all().filter(id=id, client_email=request.user.email)[0]
                # item.shipping_price = data1[id]
                # if shipping == "air":
                #     item.shipping_choose = "Air"
                # if shipping == "sea1":
                #     item.shipping_choose = "Sea 1"
                # if shipping == "sea2":
                #     item.shipping_choose = "Sea 2"
                # item.shipping_rate = rate
                # item.shipping_country = country
                # item.save()
            return JsonResponse(status = 302 , data = {'success' : f"https://toyyibpay.com/{bill_code}" })


        else:
            data = {
            'userSecretKey' : 'lctchung-fg0p-uubc-qlpt-iqg51fc1954s',
            'categoryCode' : '6elrtbk8',
            'billName' : 'Purchase from Tolongbeli',
            'billDescription' : "Shipping fee for product(s) "+ ", ".join(ids),
            'billPriceSetting' : 1,
            'billPayorInfo' : 0,
            'billAmount' : price*100,
            'billReturnUrl' : 'http://103.171.26.128:8001/my_orders',
            'billCallbackUrl' : 'http://103.171.26.128:8001/my_orders',
            'billExternalReferenceNo' : "MY"+str_id,
            'billTo' : request.user.username,
            'billEmail' : request.user.email,
            'billPhone' : "",
            'billSplitPayment' : 0,
            'billSplitPaymentArgs' : '',
            'billPaymentChannel' : '0',
            'billContentEmail' : 'Thank you for purchasing our product!',
            'billChargeToCustomer' : 2,
            }
            req = requests.post('https://toyyibpay.com/index.php/api/createBill', data=data)

            bill_code = json.loads(req.text)[0]['BillCode']



            bill = shipping_bills.objects.create(
                product_ids = json.dumps(ids),
                bill_code = bill_code,
                client_email=request.user.email,
                client_id=str_id,
                notes=f"Total was {price} - 0 paid from balance;"
            )
            bill.save()


            shipping_product = shipping.objects.create(
                sold_ids = json.dumps(ids),
                shipping_price = price,
                client_email=request.user.email,
                client_id=str_id,
                shipping_choose = shipping_choose,
                shipping_rate= rate,
                shipping_country= country,
                address= address,
                phone= phone,
                name= name,
                postcode= postcode,
            )
            shipping_product.save()

            return JsonResponse(status = 302 , data = {'success' : f"https://toyyibpay.com/{bill_code}" })


@csrf_exempt
def calculate_shipping_price(request):
    if request.method == "POST":
        dict = json.loads(request.POST.get("Products"))
        ids = dict['ids']
        rate = dict['rate']
        country = dict['country']
        shippingi = dict['shipping']
        dict_n = {}
        print(country)
        allowed_shippment = allow_shipping.objects.all()[0]


        if shippingi == "air":
            if country == "Malaysia1" and allowed_shippment.air_west_malaysia == False:
                    return JsonResponse(status=404, data={'error': f"West Malaysia can't use air shipping!"})
            if country == "Malaysia2" and allowed_shippment.air_east_malaysia == False:
                    return JsonResponse(status=404, data={'error': f"East Malaysia can't use air shipping!"})
            if country == "Singapore" and allowed_shippment.air_singapore == False:
                    return JsonResponse(status=404, data={'error': f"Singapore can't use air shipping!"})
            if country == "Brunel" and allowed_shippment.air_brunei == False:
                    return JsonResponse(status=404, data={'error': f"Brunel can't use air shipping!"})
        if shippingi == "sea1":
            if country == "Malaysia1" and allowed_shippment.sea_bulky_west_malaysia == False:
                    return JsonResponse(status=404, data={'error': f"West Malaysia can't use this sea shipping!"})
            if country == "Malaysia2" and allowed_shippment.sea_bulky_east_malaysia == False:
                    return JsonResponse(status=404, data={'error': f"East Malaysia can't use sea shipping!"})
            if country == "Singapore" and allowed_shippment.sea_bulky_singapore == False:
                    return JsonResponse(status=404, data={'error': f"Singapore can't use sea shipping!"})
            if country == "Brunel" and allowed_shippment.sea_bulky_brunei == False:
                    return JsonResponse(status=404, data={'error': f"Brunel can't use sea shipping!"})
        if shippingi == "sea2":
            print(allowed_shippment.sea_small_east_malaysia)
            if country == "Malaysia1" and allowed_shippment.sea_small_west_malaysia == False:
                    return JsonResponse(status=404, data={'error': f"West Malaysia can't use sea shipping!"})
            if country == "Malaysia2" and allowed_shippment.sea_small_east_malaysia == False:
                    return JsonResponse(status=404, data={'error': f"East Malaysia can't use sea shipping!"})
            if country == "Singapore" and allowed_shippment.sea_small_singapore == False:
                    return JsonResponse(status=404, data={'error': f"Singapore can't use sea shipping!"})
            if country == "Brunel" and allowed_shippment.sea_small_brunei == False:
                    return JsonResponse(status=404, data={'error': f"Brunel can't use sea shipping!"})
        for shipping_type in ['air', 'sea1', 'sea2']:
            w1 = 0
            w2 = 0

            for nr,id in enumerate(ids):

                item = sold.objects.all().filter(id=id, client_email=request.user.email)[0]
                # if shipping_type == "air":
                #     if item.allow_air == False:
                #         return JsonResponse(status=404, data={'error': f"Product {id} can't be shipped with {shipping_type}"})
                # if shipping_type == "sea1":
                #     if item.allow_sea_1 == False:
                #         return JsonResponse(status=404, data={'error': f"Product {id} can't be shipped with {shipping_type}"})
                # if shipping_type == "sea2":
                #     if item.allow_sea_2 == False:
                #         return JsonResponse(status=404, data={'error': f"Product {id} can't be shipped with {shipping_type}"})


                item = sold.objects.all().filter(id=id, client_email=request.user.email)[0]

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

                length = item.length
                width = item.width
                height = item.height
                weight = item.weight

                #################### AIR SHIPPING
                if shipping_type == "air":

                    w1 += math.ceil(float(length) * float(width) * float(height) / air_number)
                    w2 += math.ceil(float(weight))
                #################### SEA SHIPPING
                if shipping_type == "sea1":

                    w1 += math.ceil(float(length) * float(width) * float(height) / sea_1_number) / 10
                    w2_b = math.ceil(float(weight))


                    w2 += math.ceil(w2_b / 40) / 10



                #################### SEA 2 SHIPPING

                if shipping_type == "sea2":
                    w1 += math.ceil(float(length) * float(width) * float(height) / sea_2_number)
                    w2 += math.ceil(float(weight))




            if shipping_type == "air":

                if rate == "Normal":
                    rm = normal
                elif rate == "Sensitive":
                    rm = sensitive
                if w1 > w2:
                    air_price = w1 * rm + (w1 * rm * markup)
                else:
                    air_price = w2 * rm + (w2 * rm * markup)

                dict_n['air'] = round(air_price, 2)

            #################### SEA SHIPPING
            if shipping_type == "sea1":

                if w1 < sea_1_min:
                    w1 = sea_1_min

                if w2 < sea_1_min:
                    w2 = sea_1_min

                if w1 > w2:
                    sea_1_price = (w1 - sea_1_min) * sea_1_price_over_min + sea_1_price_under_min
                else:
                    sea_1_price = (w2 - sea_1_min) * sea_1_price_over_min + sea_1_price_under_min

                dict_n['sea1'] = round(sea_1_price, 2)

            #################### SEA 2 SHIPPING

            if shipping_type == "sea2":

                if w1 < sea_2_min:
                    w1 = sea_2_min
                if w2 < sea_2_min:
                    w2 = sea_2_min
                if w1 > w2:
                    sea_2_price = (w1 - sea_2_min) * sea_2_price_over_min + sea_2_price_under_min
                else:
                    sea_2_price = (w2 - sea_2_min) * sea_2_price_over_min + sea_2_price_under_min

                dict_n['sea2'] = round(sea_2_price, 2)

        return JsonResponse(status=302, data={"prices":dict_n})


@login_required(login_url=login_page)
def recharge(request):
    if request.method == "POST":
        amount = float(request.POST.get("charge_number"))

        str_id = str(request.user.id)
        while len(str_id) < 6:
            str_id = "0"+str_id

            data = {
            'userSecretKey' : 'lctchung-fg0p-uubc-qlpt-iqg51fc1954s',
            'categoryCode' : '6elrtbk8',
            'billName' : 'Purchase from Tolongbeli',
            'billDescription' : "Recharging your wallet",
            'billPriceSetting' : 1,
            'billPayorInfo' : 0,
            'billAmount' : amount*100,
            'billReturnUrl' : 'http://103.171.26.128:8001/my_orders',
            'billCallbackUrl' : 'http://103.171.26.128:8001/my_orders',
            'billExternalReferenceNo' : "MY"+str_id,
            'billTo' : request.user.username,
            'billEmail' : request.user.email,
            'billPhone' : "",
            'billSplitPayment' : 0,
            'billSplitPaymentArgs' : '',
            'billPaymentChannel' : '0',
            'billContentEmail' : 'Thank you for the recharge!',
            'billChargeToCustomer' : 2,
            }
            req = requests.post('https://toyyibpay.com/index.php/api/createBill', data=data)

            bill_code = json.loads(req.text)[0]['BillCode']

            bill = recharge_bills.objects.create(
                bill_code=bill_code,
                client_email=request.user.email,
                client_id=str_id,
                amount=amount
            )
            bill.save()
            return HttpResponseRedirect(f"https://toyyibpay.com/{bill_code}")


