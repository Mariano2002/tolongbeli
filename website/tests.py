from django.test import TestCase
import requests
import json

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
    ('itemid', '506134747'),
    ('shopid', '23261849'),
    ('state', 'JAWA BARAT'),
    ('town', ''),
)

response = requests.get('https://shopee.co.id/api/v4/pdp/get_shipping_info', headers=headers, params=params)
print(response.text)

shipping_name = ""
shipping_price = None
for i in response.json()['data']['shipping_infos']:
    try:
        if int(i['cost_info']['estimated_shipping_fee']) < shipping_price:
            shipping_price = int(i['cost_info']['estimated_shipping_fee'])
            shipping_name = i['channel']['name']
    except:
        shipping_price = int(i['cost_info']['estimated_shipping_fee'])
        shipping_name = i['channel']['name']
print(shipping_price)
input()
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
    'referer': f'https://www.tokopedia.com/agusidstoreapple/asus-tuf-f15-fx506lh-i5-10300h-nvidia-gtx1650-144hz-8gb-512gb-ssd-w10',
    'accept-language': 'en-US,en;q=0.9',
}

api_key = "jJcauPNv4W2rg75x3tHGsbVqZAyLCpEY"
proxy_url = "http://falcon.proxyrotator.com:51337/?apiKey={}&userAgent=true&get=true&post=true".format(api_key)


def getProxy():
    try:
        r = requests.get(proxy_url, timeout=5)
        js = json.loads(r.text)
        # , js['randomUserAgent']
        return js['proxy']
    except Exception as e:
        pass

while True:
    try:
        proxy = getProxy()
        print(proxy)
        proxies = {'https': 'https://' + proxy}

        req = requests.get("https://www.tokopedia.com/agusidstoreapple/asus-tuf-f15-fx506lh-i5-10300h-nvidia-gtx1650-144hz-8gb-512gb-ssd-w10", headers=headers, proxies=proxies, timeout=5)

        print(req.text)
        break
    except:
        pass


'''
[{"data":{"pdpGetLayout":{"name":"Default Layout Desktop","pdpSession":"{\"sid\":1168087,\"sd\":\"agusidstoreapple\",\"cat\":{\"id\":4008},\"pid\":1186331168,\"cp\":{},\"pr\":13569000,\"mo\":1,\"pn\":\"ASUS TUF F15 FX506LH i5-10300H Nvidia GTX1650 144Hz 8GB 512GB SSD W10\",\"cn\":\"new\",\"li\":1,\"w\":7,\"sf\":{\"iga\":false,\"itn\":false},\"v\":1,\"vd\":{\"2002629267\":{\"cp\":{},\"s\":8,\"ib\":true,\"whid\":3978559,\"mo\":1},\"2002629268\":{\"cp\":{},\"s\":1,\"whid\":3978559,\"mo\":1},\"2002629269\":{\"cp\":{},\"s\":1,\"whid\":3978559,\"mo\":1},\"2002629270\":{\"cp\":{},\"s\":1,\"whid\":3978559,\"mo\":1},\"2002629271\":{\"cp\":{},\"s\":1,\"whid\":3978559,\"mo\":1},\"2002629272\":{\"cp\":{},\"s\":1,\"whid\":3978559,\"mo\":1},\"2002629273\":{\"cp\":{},\"s\":1,\"whid\":3978559,\"mo\":1},\"2002629274\":{\"cp\":{},\"s\":1,\"whid\":3978559,\"mo\":1},\"2002629275\":{\"cp\":{},\"s\":1,\"whid\":3978559,\"mo\":1},\"2002629276\":{\"cp\":{},\"s\":1,\"whid\":3978559,\"mo\":1},\"2002629277\":{\"cp\":{},\"s\":1,\"whid\":3978559,\"mo\":1},\"2002629278\":{\"cp\":{},\"s\":1,\"whid\":3978559,\"mo\":1},\"2002629279\":{\"cp\":{},\"s\":1,\"whid\":3978559,\"mo\":1}},\"pi\":1186331168,\"pse\":1,\"ps\":\"ACTIVE\",\"ipr\":true}","basicInfo":{"alias":"asus-tuf-f15-fx506lh-i5-10300h-nvidia-gtx1650-144hz-8gb-512gb-ssd-w10","isQA":false,"id":"1186331168","shopID":"1168087","shopName":"agusidstoreapple","minOrder":1,"maxOrder":0,"weight":7000,"weightUnit":"GRAM","condition":"NEW","status":"ACTIVE","url":"https://www.tokopedia.com/agusidstoreapple/asus-tuf-f15-fx506lh-i5-10300h-nvidia-gtx1650-144hz-8gb-512gb-ssd-w10","needPrescription":false,"catalogID":"0","isLeasing":false,"isBlacklisted":false,"menu":{"id":"29135095","name":"LAPTOP ASUS GAMING","url":"https://www.tokopedia.com/agusidstoreapple/etalase/laptop-asus-gaming","__typename":"pdpMenu"},"category":{"id":"4008","name":"Laptop Gaming","title":"Laptop Gaming","breadcrumbURL":"https://www.tokopedia.com/p/komputer-laptop/pc-laptop-gaming/laptop-gaming","isAdult":false,"detail":[{"id":"297","name":"Komputer \u0026 Laptop","breadcrumbURL":"https://www.tokopedia.com/p/komputer-laptop","isAdult":false,"__typename":"pdpCategoryDetail"},{"id":"3847","name":"PC \u0026 Laptop Gaming","breadcrumbURL":"https://www.tokopedia.com/p/komputer-laptop/pc-laptop-gaming","isAdult":false,"__typename":"pdpCategoryDetail"},{"id":"4008","name":"Laptop Gaming","breadcrumbURL":"https://www.tokopedia.com/p/komputer-laptop/pc-laptop-gaming/laptop-gaming","isAdult":false,"__typename":"pdpCategoryDetail"}],"__typename":"pdpCategory"},"txStats":{"transactionSuccess":"57","transactionReject":"1","countSold":"58","paymentVerified":"65","itemSoldPaymentVerified":"58","__typename":"txStats"},"stats":{"countView":"23146","countReview":"46","countTalk":"32","rating":5,"__typename":"pdpStats"},"__typename":"pdpBasicInfo"},"components":[{"name":"product_media","type":"product_media","position":"[0,0,1,4]","data":[{"media":[{"type":"image","urlThumbnail":"https://images.tokopedia.net/img/cache/200-square/VqbcmM/2021/7/29/e6737894-0385-447f-a7ee-6b60322fa5c0.png","videoUrl":"","prefix":"https://images.tokopedia.net/img/cache/","suffix":"/VqbcmM/2021/7/29/e6737894-0385-447f-a7ee-6b60322fa5c0.png","description":"","__typename":"pdpContentSnapshotMedia"},{"type":"image","urlThumbnail":"https://images.tokopedia.net/img/cache/200-square/VqbcmM/2021/7/29/73a6baf7-4862-453e-9360-5b3a7e9b9ff3.jpg","videoUrl":"","prefix":"https://images.tokopedia.net/img/cache/","suffix":"/VqbcmM/2021/7/29/73a6baf7-4862-453e-9360-5b3a7e9b9ff3.jpg","description":"","__typename":"pdpContentSnapshotMedia"},{"type":"image","urlThumbnail":"https://images.tokopedia.net/img/cache/200-square/VqbcmM/2021/7/29/ac17fb02-48a4-4009-805a-fbd3779c5b68.jpg","videoUrl":"","prefix":"https://images.tokopedia.net/img/cache/","suffix":"/VqbcmM/2021/7/29/ac17fb02-48a4-4009-805a-fbd3779c5b68.jpg","description":"","__typename":"pdpContentSnapshotMedia"},{"type":"image","urlThumbnail":"https://images.tokopedia.net/img/cache/200-square/VqbcmM/2021/7/29/332c282e-2e5f-4a5a-ba0f-453bc412966e.jpg","videoUrl":"","prefix":"https://images.tokopedia.net/img/cache/","suffix":"/VqbcmM/2021/7/29/332c282e-2e5f-4a5a-ba0f-453bc412966e.jpg","description":"","__typename":"pdpContentSnapshotMedia"},{"type":"image","urlThumbnail":"https://images.tokopedia.net/img/cache/200-square/VqbcmM/2021/7/29/2f0939e4-d9d3-4a10-ad3e-715e43990a5c.jpg","videoUrl":"","prefix":"https://images.tokopedia.net/img/cache/","suffix":"/VqbcmM/2021/7/29/2f0939e4-d9d3-4a10-ad3e-715e43990a5c.jpg","description":"","__typename":"pdpContentSnapshotMedia"}],"videos":[{"source":"youtube","url":"9mVTOqlmuw0","__typename":"pdpContentSnapshotVideos"}],"__typename":"pdpDataProductMedia","__typename":"pdpDataProductMedia"}],"__typename":"pdpComponent"},{"name":"ticker_info","type":"ticker_info","position":"[1,0,1,1]","data":[],"__typename":"pdpComponent"},{"name":"variant_options","type":"variant","position":"[2,0,1,4]","data":[{"errorCode":0,"parentID":"1186331168","defaultChild":"2002629267","sizeChart":"","variants":[{"productVariantID":"21055888","variantID":"1","name":"warna","identifier":"colour","option":[{"picture":{"urlOriginal":"","urlThumbnail":"","__typename":"pdpProductVariantPicture"},"productVariantOptionID":"129247996","variantUnitValueID":"0","value":"NON Bundle","hex":"","__typename":"pdpProductVariantOption"},{"picture":{"urlOriginal":"","urlThumbnail":"","__typename":"pdpProductVariantPicture"},"productVariantOptionID":"129248000","variantUnitValueID":"0","value":"Bundle HS B","hex":"","__typename":"pdpProductVariantOption"},{"picture":{"urlOriginal":"","urlThumbnail":"","__typename":"pdpProductVariantPicture"},"productVariantOptionID":"129248005","variantUnitValueID":"0","value":"Bundle M+H A","hex":"","__typename":"pdpProductVariantOption"},{"picture":{"urlOriginal":"","urlThumbnail":"","__typename":"pdpProductVariantPicture"},"productVariantOptionID":"129247997","variantUnitValueID":"0","value":"Bundle MOUSE A","hex":"","__typename":"pdpProductVariantOption"},{"picture":{"urlOriginal":"","urlThumbnail":"","__typename":"pdpProductVariantPicture"},"productVariantOptionID":"129247998","variantUnitValueID":"0","value":"Bundle HS A","hex":"","__typename":"pdpProductVariantOption"},{"picture":{"urlOriginal":"","urlThumbnail":"","__typename":"pdpProductVariantPicture"},"productVariantOptionID":"129248007","variantUnitValueID":"0","value":"Bundle M+H C","hex":"","__typename":"pdpProductVariantOption"},{"picture":{"urlOriginal":"","urlThumbnail":"","__typename":"pdpProductVariantPicture"},"productVariantOptionID":"129248004","variantUnitValueID":"0","value":"Bundle HS D","hex":"","__typename":"pdpProductVariantOption"},{"picture":{"urlOriginal":"","urlThumbnail":"","__typename":"pdpProductVariantPicture"},"productVariantOptionID":"129248003","variantUnitValueID":"0","value":"Bundle MOUSE D","hex":"","__typename":"pdpProductVariantOption"},{"picture":{"urlOriginal":"","urlThumbnail":"","__typename":"pdpProductVariantPicture"},"productVariantOptionID":"129248006","variantUnitValueID":"0","value":"Bundle M+H B","hex":"","__typename":"pdpProductVariantOption"},{"picture":{"urlOriginal":"","urlThumbnail":"","__typename":"pdpProductVariantPicture"},"productVariantOptionID":"129248008","variantUnitValueID":"0","value":"Bundle M+H D","hex":"","__typename":"pdpProductVariantOption"},{"picture":{"urlOriginal":"","urlThumbnail":"","__typename":"pdpProductVariantPicture"},"productVariantOptionID":"129248002","variantUnitValueID":"0","value":"Bundle HS C","hex":"","__typename":"pdpProductVariantOption"},{"picture":{"urlOriginal":"","urlThumbnail":"","__typename":"pdpProductVariantPicture"},"productVariantOptionID":"129247999","variantUnitValueID":"0","value":"Bundle MOUSE B","hex":"","__typename":"pdpProductVariantOption"},{"picture":{"urlOriginal":"","urlThumbnail":"","__typename":"pdpProductVariantPicture"},"productVariantOptionID":"129248001","variantUnitValueID":"0","value":"Bundle MOUSE C","hex":"","__typename":"pdpProductVariantOption"}],"__typename":"pdpProductVariantOutput"}],"children":[{"productID":"2002629267","price":13569000,"priceFmt":"Rp 0","optionID":[129247996],"productName":"ASUS TUF F15 FX506LH i5-10300H Nvidia GTX1650 144Hz 8GB 512GB SSD W10 - NON Bundle","productURL":"https://www.tokopedia.com/agusidstoreapple/asus-tuf-f15-fx506lh-i5-10300h-nvidia-gtx1650-144hz-8gb-512gb-ssd-w10-non-bundle","picture":{"urlOriginal":"https://images.tokopedia.net/img/cache/700/VqbcmM/2021/7/29/e6737894-0385-447f-a7ee-6b60322fa5c0.png","urlThumbnail":"https://images.tokopedia.net/img/cache/100-square/VqbcmM/2021/7/29/e6737894-0385-447f-a7ee-6b60322fa5c0.png","__typename":"pdpProductVariantPicture"},"stock":{"stock":"8","isBuyable":true,"stockWordingHTML":"Stok \u003cb\u003etersisa \u0026lt;10,\u003c/b\u003e beli segera!","minimumOrder":"1","maximumOrder":"8","__typename":"pdpProductVariantStock"},"isCOD":false,"isWishlist":false,"campaignInfo":{"campaignID":"0","campaignType":"0","campaignTypeName":"","campaignIdentifier":0,"background":"","discountPercentage":0,"originalPrice":0,"discountPrice":0,"stock":0,"stockSoldPercentage":0,"startDate":"","endDate":"","endDateUnix":"0","appLinks":"","isAppsOnly":false,"isActive":false,"hideGimmick":false,"isCheckImei":false,"__typename":"pdpProductVariantCampaign"},"thematicCampaign":{"additionalInfo":"","background":"","campaignName":"","icon":"","__typename":"pdpContentSnapshotThematicCampaign"},"__typename":"pdpProductVariantChildren"},{"productID":"2002629268","price":13399000,"priceFmt":"Rp 0","optionID":[129247997],"productName":"ASUS TUF F15 FX506LH i5-10300H Nvidia GTX1650 144Hz 8GB 512GB SSD W10 - Bundle MOUSE A","productURL":"https://www.tokopedia.com/agusidstoreapple/asus-tuf-f15-fx506lh-i5-10300h-nvidia-gtx1650-144hz-8gb-512gb-ssd-w10-bundle-mouse-a","picture":{"urlOriginal":"https://images.tokopedia.net/img/cache/700/VqbcmM/2021/7/29/e6737894-0385-447f-a7ee-6b60322fa5c0.png","urlThumbnail":"https://images.tokopedia.net/img/cache/100-square/VqbcmM/2021/7/29/e6737894-0385-447f-a7ee-6b60322fa5c0.png","__typename":"pdpProductVariantPicture"},"stock":{"stock":"1","isBuyable":false,"stockWordingHTML":"\u003cb style='color:red'\u003eStok terakhir,\u003c/b\u003e beli sekarang!","minimumOrder":"1","maximumOrder":"1","__typename":"pdpProductVariantStock"},"isCOD":false,"isWishlist":false,"campaignInfo":{"campaignID":"0","campaignType":"0","campaignTypeName":"","campaignIdentifier":0,"background":"","discountPercentage":0,"originalPrice":0,"discountPrice":0,"stock":0,"stockSoldPercentage":0,"startDate":"","endDate":"","endDateUnix":"0","appLinks":"","isAppsOnly":false,"isActive":false,"hideGimmick":false,"isCheckImei":false,"__typename":"pdpProductVariantCampaign"},"thematicCampaign":{"additionalInfo":"","background":"","campaignName":"","icon":"","__typename":"pdpContentSnapshotThematicCampaign"},"__typename":"pdpProductVariantChildren"},{"productID":"2002629269","price":13399000,"priceFmt":"Rp 0","optionID":[129247998],"productName":"ASUS TUF F15 FX506LH i5-10300H Nvidia GTX1650 144Hz 8GB 512GB SSD W10 - Bundle HS A","productURL":"https://www.tokopedia.com/agusidstoreapple/asus-tuf-f15-fx506lh-i5-10300h-nvidia-gtx1650-144hz-8gb-512gb-ssd-w10-bundle-hs-a","picture":{"urlOriginal":"https://images.tokopedia.net/img/cache/700/VqbcmM/2021/7/29/e6737894-0385-447f-a7ee-6b60322fa5c0.png","urlThumbnail":"https://images.tokopedia.net/img/cache/100-square/VqbcmM/2021/7/29/e6737894-0385-447f-a7ee-6b60322fa5c0.png","__typename":"pdpProductVariantPicture"},"stock":{"stock":"1","isBuyable":false,"stockWordingHTML":"\u003cb style='color:red'\u003eStok terakhir,\u003c/b\u003e beli sekarang!","minimumOrder":"1","maximumOrder":"1","__typename":"pdpProductVariantStock"},"isCOD":false,"isWishlist":false,"campaignInfo":{"campaignID":"0","campaignType":"0","campaignTypeName":"","campaignIdentifier":0,"background":"","discountPercentage":0,"originalPrice":0,"discountPrice":0,"stock":0,"stockSoldPercentage":0,"startDate":"","endDate":"","endDateUnix":"0","appLinks":"","isAppsOnly":false,"isActive":false,"hideGimmick":false,"isCheckImei":false,"__typename":"pdpProductVariantCampaign"},"thematicCampaign":{"additionalInfo":"","background":"","campaignName":"","icon":"","__typename":"pdpContentSnapshotThematicCampaign"},"__typename":"pdpProductVariantChildren"},{"productID":"2002629270","price":13699000,"priceFmt":"Rp 0","optionID":[129247999],"productName":"ASUS TUF F15 FX506LH i5-10300H Nvidia GTX1650 144Hz 8GB 512GB SSD W10 - Bundle MOUSE B","productURL":"https://www.tokopedia.com/agusidstoreapple/asus-tuf-f15-fx506lh-i5-10300h-nvidia-gtx1650-144hz-8gb-512gb-ssd-w10-bundle-mouse-b","picture":{"urlOriginal":"https://images.tokopedia.net/img/cache/700/VqbcmM/2021/7/29/e6737894-0385-447f-a7ee-6b60322fa5c0.png","urlThumbnail":"https://images.tokopedia.net/img/cache/100-square/VqbcmM/2021/7/29/e6737894-0385-447f-a7ee-6b60322fa5c0.png","__typename":"pdpProductVariantPicture"},"stock":{"stock":"1","isBuyable":false,"stockWordingHTML":"\u003cb style='color:red'\u003eStok terakhir,\u003c/b\u003e beli sekarang!","minimumOrder":"1","maximumOrder":"1","__typename":"pdpProductVariantStock"},"isCOD":false,"isWishlist":false,"campaignInfo":{"campaignID":"0","campaignType":"0","campaignTypeName":"","campaignIdentifier":0,"background":"","discountPercentage":0,"originalPrice":0,"discountPrice":0,"stock":0,"stockSoldPercentage":0,"startDate":"","endDate":"","endDateUnix":"0","appLinks":"","isAppsOnly":false,"isActive":false,"hideGimmick":false,"isCheckImei":false,"__typename":"pdpProductVariantCampaign"},"thematicCampaign":{"additionalInfo":"","background":"","campaignName":"","icon":"","__typename":"pdpContentSnapshotThematicCampaign"},"__typename":"pdpProductVariantChildren"},{"productID":"2002629271","price":13699000,"priceFmt":"Rp 0","optionID":[129248000],"productName":"ASUS TUF F15 FX506LH i5-10300H Nvidia GTX1650 144Hz 8GB 512GB SSD W10 - Bundle HS B","productURL":"https://www.tokopedia.com/agusidstoreapple/asus-tuf-f15-fx506lh-i5-10300h-nvidia-gtx1650-144hz-8gb-512gb-ssd-w10-bundle-hs-b","picture":{"urlOriginal":"https://images.tokopedia.net/img/cache/700/VqbcmM/2021/7/29/e6737894-0385-447f-a7ee-6b60322fa5c0.png","urlThumbnail":"https://images.tokopedia.net/img/cache/100-square/VqbcmM/2021/7/29/e6737894-0385-447f-a7ee-6b60322fa5c0.png","__typename":"pdpProductVariantPicture"},"stock":{"stock":"1","isBuyable":false,"stockWordingHTML":"\u003cb style='color:red'\u003eStok terakhir,\u003c/b\u003e beli sekarang!","minimumOrder":"1","maximumOrder":"1","__typename":"pdpProductVariantStock"},"isCOD":false,"isWishlist":false,"campaignInfo":{"campaignID":"0","campaignType":"0","campaignTypeName":"","campaignIdentifier":0,"background":"","discountPercentage":0,"originalPrice":0,"discountPrice":0,"stock":0,"stockSoldPercentage":0,"startDate":"","endDate":"","endDateUnix":"0","appLinks":"","isAppsOnly":false,"isActive":false,"hideGimmick":false,"isCheckImei":false,"__typename":"pdpProductVariantCampaign"},"thematicCampaign":{"additionalInfo":"","background":"","campaignName":"","icon":"","__typename":"pdpContentSnapshotThematicCampaign"},"__typename":"pdpProductVariantChildren"},{"productID":"2002629272","price":13899000,"priceFmt":"Rp 0","optionID":[129248001],"productName":"ASUS TUF F15 FX506LH i5-10300H Nvidia GTX1650 144Hz 8GB 512GB SSD W10 - Bundle MOUSE C","productURL":"https://www.tokopedia.com/agusidstoreapple/asus-tuf-f15-fx506lh-i5-10300h-nvidia-gtx1650-144hz-8gb-512gb-ssd-w10-bundle-mouse-c","picture":{"urlOriginal":"https://images.tokopedia.net/img/cache/700/VqbcmM/2021/7/29/e6737894-0385-447f-a7ee-6b60322fa5c0.png","urlThumbnail":"https://images.tokopedia.net/img/cache/100-square/VqbcmM/2021/7/29/e6737894-0385-447f-a7ee-6b60322fa5c0.png","__typename":"pdpProductVariantPicture"},"stock":{"stock":"1","isBuyable":false,"stockWordingHTML":"\u003cb style='color:red'\u003eStok terakhir,\u003c/b\u003e beli sekarang!","minimumOrder":"1","maximumOrder":"1","__typename":"pdpProductVariantStock"},"isCOD":false,"isWishlist":false,"campaignInfo":{"campaignID":"0","campaignType":"0","campaignTypeName":"","campaignIdentifier":0,"background":"","discountPercentage":0,"originalPrice":0,"discountPrice":0,"stock":0,"stockSoldPercentage":0,"startDate":"","endDate":"","endDateUnix":"0","appLinks":"","isAppsOnly":false,"isActive":false,"hideGimmick":false,"isCheckImei":false,"__typename":"pdpProductVariantCampaign"},"thematicCampaign":{"additionalInfo":"","background":"","campaignName":"","icon":"","__typename":"pdpContentSnapshotThematicCampaign"},"__typename":"pdpProductVariantChildren"},{"productID":"2002629273","price":13899000,"priceFmt":"Rp 0","optionID":[129248002],"productName":"ASUS TUF F15 FX506LH i5-10300H Nvidia GTX1650 144Hz 8GB 512GB SSD W10 - Bundle HS C","productURL":"https://www.tokopedia.com/agusidstoreapple/asus-tuf-f15-fx506lh-i5-10300h-nvidia-gtx1650-144hz-8gb-512gb-ssd-w10-bundle-hs-c","picture":{"urlOriginal":"https://images.tokopedia.net/img/cache/700/VqbcmM/2021/7/29/e6737894-0385-447f-a7ee-6b60322fa5c0.png","urlThumbnail":"https://images.tokopedia.net/img/cache/100-square/VqbcmM/2021/7/29/e6737894-0385-447f-a7ee-6b60322fa5c0.png","__typename":"pdpProductVariantPicture"},"stock":{"stock":"1","isBuyable":false,"stockWordingHTML":"\u003cb style='color:red'\u003eStok terakhir,\u003c/b\u003e beli sekarang!","minimumOrder":"1","maximumOrder":"1","__typename":"pdpProductVariantStock"},"isCOD":false,"isWishlist":false,"campaignInfo":{"campaignID":"0","campaignType":"0","campaignTypeName":"","campaignIdentifier":0,"background":"","discountPercentage":0,"originalPrice":0,"discountPrice":0,"stock":0,"stockSoldPercentage":0,"startDate":"","endDate":"","endDateUnix":"0","appLinks":"","isAppsOnly":false,"isActive":false,"hideGimmick":false,"isCheckImei":false,"__typename":"pdpProductVariantCampaign"},"thematicCampaign":{"additionalInfo":"","background":"","campaignName":"","icon":"","__typename":"pdpContentSnapshotThematicCampaign"},"__typename":"pdpProductVariantChildren"},{"productID":"2002629274","price":14399000,"priceFmt":"Rp 0","optionID":[129248003],"productName":"ASUS TUF F15 FX506LH i5-10300H Nvidia GTX1650 144Hz 8GB 512GB SSD W10 - Bundle MOUSE D","productURL":"https://www.tokopedia.com/agusidstoreapple/asus-tuf-f15-fx506lh-i5-10300h-nvidia-gtx1650-144hz-8gb-512gb-ssd-w10-bundle-mouse-d","picture":{"urlOriginal":"https://images.tokopedia.net/img/cache/700/VqbcmM/2021/7/29/e6737894-0385-447f-a7ee-6b60322fa5c0.png","urlThumbnail":"https://images.tokopedia.net/img/cache/100-square/VqbcmM/2021/7/29/e6737894-0385-447f-a7ee-6b60322fa5c0.png","__typename":"pdpProductVariantPicture"},"stock":{"stock":"1","isBuyable":false,"stockWordingHTML":"\u003cb style='color:red'\u003eStok terakhir,\u003c/b\u003e beli sekarang!","minimumOrder":"1","maximumOrder":"1","__typename":"pdpProductVariantStock"},"isCOD":false,"isWishlist":false,"campaignInfo":{"campaignID":"0","campaignType":"0","campaignTypeName":"","campaignIdentifier":0,"background":"","discountPercentage":0,"originalPrice":0,"discountPrice":0,"stock":0,"stockSoldPercentage":0,"startDate":"","endDate":"","endDateUnix":"0","appLinks":"","isAppsOnly":false,"isActive":false,"hideGimmick":false,"isCheckImei":false,"__typename":"pdpProductVariantCampaign"},"thematicCampaign":{"additionalInfo":"","background":"","campaignName":"","icon":"","__typename":"pdpContentSnapshotThematicCampaign"},"__typename":"pdpProductVariantChildren"},{"productID":"2002629275","price":14399000,"priceFmt":"Rp 0","optionID":[129248004],"productName":"ASUS TUF F15 FX506LH i5-10300H Nvidia GTX1650 144Hz 8GB 512GB SSD W10 - Bundle HS D","productURL":"https://www.tokopedia.com/agusidstoreapple/asus-tuf-f15-fx506lh-i5-10300h-nvidia-gtx1650-144hz-8gb-512gb-ssd-w10-bundle-hs-d","picture":{"urlOriginal":"https://images.tokopedia.net/img/cache/700/VqbcmM/2021/7/29/e6737894-0385-447f-a7ee-6b60322fa5c0.png","urlThumbnail":"https://images.tokopedia.net/img/cache/100-square/VqbcmM/2021/7/29/e6737894-0385-447f-a7ee-6b60322fa5c0.png","__typename":"pdpProductVariantPicture"},"stock":{"stock":"1","isBuyable":false,"stockWordingHTML":"\u003cb style='color:red'\u003eStok terakhir,\u003c/b\u003e beli sekarang!","minimumOrder":"1","maximumOrder":"1","__typename":"pdpProductVariantStock"},"isCOD":false,"isWishlist":false,"campaignInfo":{"campaignID":"0","campaignType":"0","campaignTypeName":"","campaignIdentifier":0,"background":"","discountPercentage":0,"originalPrice":0,"discountPrice":0,"stock":0,"stockSoldPercentage":0,"startDate":"","endDate":"","endDateUnix":"0","appLinks":"","isAppsOnly":false,"isActive":false,"hideGimmick":false,"isCheckImei":false,"__typename":"pdpProductVariantCampaign"},"thematicCampaign":{"additionalInfo":"","background":"","campaignName":"","icon":"","__typename":"pdpContentSnapshotThematicCampaign"},"__typename":"pdpProductVariantChildren"},{"productID":"2002629276","price":13899000,"priceFmt":"Rp 0","optionID":[129248005],"productName":"ASUS TUF F15 FX506LH i5-10300H Nvidia GTX1650 144Hz 8GB 512GB SSD W10 - Bundle M+H A","productURL":"https://www.tokopedia.com/agusidstoreapple/asus-tuf-f15-fx506lh-i5-10300h-nvidia-gtx1650-144hz-8gb-512gb-ssd-w10-bundle-m-h-a","picture":{"urlOriginal":"https://images.tokopedia.net/img/cache/700/VqbcmM/2021/7/29/e6737894-0385-447f-a7ee-6b60322fa5c0.png","urlThumbnail":"https://images.tokopedia.net/img/cache/100-square/VqbcmM/2021/7/29/e6737894-0385-447f-a7ee-6b60322fa5c0.png","__typename":"pdpProductVariantPicture"},"stock":{"stock":"1","isBuyable":false,"stockWordingHTML":"\u003cb style='color:red'\u003eStok terakhir,\u003c/b\u003e beli sekarang!","minimumOrder":"1","maximumOrder":"1","__typename":"pdpProductVariantStock"},"isCOD":false,"isWishlist":false,"campaignInfo":{"campaignID":"0","campaignType":"0","campaignTypeName":"","campaignIdentifier":0,"background":"","discountPercentage":0,"originalPrice":0,"discountPrice":0,"stock":0,"stockSoldPercentage":0,"startDate":"","endDate":"","endDateUnix":"0","appLinks":"","isAppsOnly":false,"isActive":false,"hideGimmick":false,"isCheckImei":false,"__typename":"pdpProductVariantCampaign"},"thematicCampaign":{"additionalInfo":"","background":"","campaignName":"","icon":"","__typename":"pdpContentSnapshotThematicCampaign"},"__typename":"pdpProductVariantChildren"},{"productID":"2002629277","price":14499000,"priceFmt":"Rp 0","optionID":[129248006],"productName":"ASUS TUF F15 FX506LH i5-10300H Nvidia GTX1650 144Hz 8GB 512GB SSD W10 - Bundle M+H B","productURL":"https://www.tokopedia.com/agusidstoreapple/asus-tuf-f15-fx506lh-i5-10300h-nvidia-gtx1650-144hz-8gb-512gb-ssd-w10-bundle-m-h-b","picture":{"urlOriginal":"https://images.tokopedia.net/img/cache/700/VqbcmM/2021/7/29/e6737894-0385-447f-a7ee-6b60322fa5c0.png","urlThumbnail":"https://images.tokopedia.net/img/cache/100-square/VqbcmM/2021/7/29/e6737894-0385-447f-a7ee-6b60322fa5c0.png","__typename":"pdpProductVariantPicture"},"stock":{"stock":"1","isBuyable":false,"stockWordingHTML":"\u003cb style='color:red'\u003eStok terakhir,\u003c/b\u003e beli sekarang!","minimumOrder":"1","maximumOrder":"1","__typename":"pdpProductVariantStock"},"isCOD":false,"isWishlist":false,"campaignInfo":{"campaignID":"0","campaignType":"0","campaignTypeName":"","campaignIdentifier":0,"background":"","discountPercentage":0,"originalPrice":0,"discountPrice":0,"stock":0,"stockSoldPercentage":0,"startDate":"","endDate":"","endDateUnix":"0","appLinks":"","isAppsOnly":false,"isActive":false,"hideGimmick":false,"isCheckImei":false,"__typename":"pdpProductVariantCampaign"},"thematicCampaign":{"additionalInfo":"","background":"","campaignName":"","icon":"","__typename":"pdpContentSnapshotThematicCampaign"},"__typename":"pdpProductVariantChildren"},{"productID":"2002629278","price":14899000,"priceFmt":"Rp 0","optionID":[129248007],"productName":"ASUS TUF F15 FX506LH i5-10300H Nvidia GTX1650 144Hz 8GB 512GB SSD W10 - Bundle M+H C","productURL":"https://www.tokopedia.com/agusidstoreapple/asus-tuf-f15-fx506lh-i5-10300h-nvidia-gtx1650-144hz-8gb-512gb-ssd-w10-bundle-m-h-c","picture":{"urlOriginal":"https://images.tokopedia.net/img/cache/700/VqbcmM/2021/7/29/e6737894-0385-447f-a7ee-6b60322fa5c0.png","urlThumbnail":"https://images.tokopedia.net/img/cache/100-square/VqbcmM/2021/7/29/e6737894-0385-447f-a7ee-6b60322fa5c0.png","__typename":"pdpProductVariantPicture"},"stock":{"stock":"1","isBuyable":false,"stockWordingHTML":"\u003cb style='color:red'\u003eStok terakhir,\u003c/b\u003e beli sekarang!","minimumOrder":"1","maximumOrder":"1","__typename":"pdpProductVariantStock"},"isCOD":false,"isWishlist":false,"campaignInfo":{"campaignID":"0","campaignType":"0","campaignTypeName":"","campaignIdentifier":0,"background":"","discountPercentage":0,"originalPrice":0,"discountPrice":0,"stock":0,"stockSoldPercentage":0,"startDate":"","endDate":"","endDateUnix":"0","appLinks":"","isAppsOnly":false,"isActive":false,"hideGimmick":false,"isCheckImei":false,"__typename":"pdpProductVariantCampaign"},"thematicCampaign":{"additionalInfo":"","background":"","campaignName":"","icon":"","__typename":"pdpContentSnapshotThematicCampaign"},"__typename":"pdpProductVariantChildren"},{"productID":"2002629279","price":15899000,"priceFmt":"Rp 0","optionID":[129248008],"productName":"ASUS TUF F15 FX506LH i5-10300H Nvidia GTX1650 144Hz 8GB 512GB SSD W10 - Bundle M+H D","productURL":"https://www.tokopedia.com/agusidstoreapple/asus-tuf-f15-fx506lh-i5-10300h-nvidia-gtx1650-144hz-8gb-512gb-ssd-w10-bundle-m-h-d","picture":{"urlOriginal":"https://images.tokopedia.net/img/cache/700/VqbcmM/2021/7/29/e6737894-0385-447f-a7ee-6b60322fa5c0.png","urlThumbnail":"https://images.tokopedia.net/img/cache/100-square/VqbcmM/2021/7/29/e6737894-0385-447f-a7ee-6b60322fa5c0.png","__typename":"pdpProductVariantPicture"},"stock":{"stock":"1","isBuyable":false,"stockWordingHTML":"\u003cb style='color:red'\u003eStok terakhir,\u003c/b\u003e beli sekarang!","minimumOrder":"1","maximumOrder":"1","__typename":"pdpProductVariantStock"},"isCOD":false,"isWishlist":false,"campaignInfo":{"campaignID":"0","campaignType":"0","campaignTypeName":"","campaignIdentifier":0,"background":"","discountPercentage":0,"originalPrice":0,"discountPrice":0,"stock":0,"stockSoldPercentage":0,"startDate":"","endDate":"","endDateUnix":"0","appLinks":"","isAppsOnly":false,"isActive":false,"hideGimmick":false,"isCheckImei":false,"__typename":"pdpProductVariantCampaign"},"thematicCampaign":{"additionalInfo":"","background":"","campaignName":"","icon":"","__typename":"pdpContentSnapshotThematicCampaign"},"__typename":"pdpProductVariantChildren"}],"__typename":"pdpDataProductVariant","__typename":"pdpDataProductVariant"}],"__typename":"pdpComponent"},{"name":"product_content","type":"product_content","position":"[1,1,1,1]","data":[{"name":"ASUS TUF F15 FX506LH i5-10300H Nvidia GTX1650 144Hz 8GB 512GB SSD W10","price":{"value":13569000,"currency":"IDR","__typename":"pdpContentSnapshotPrice"},"campaign":{"campaignID":"0","campaignType":"0","campaignTypeName":"","campaignIdentifier":0,"background":"","percentageAmount":0,"originalPrice":0,"discountedPrice":0,"originalStock":0,"stock":0,"stockSoldPercentage":0,"threshold":0,"startDate":"","endDate":"","endDateUnix":"0","appLinks":"","isAppsOnly":false,"isActive":false,"hideGimmick":false,"__typename":"pdpContentSnapshotCampaign"},"thematicCampaign":{"additionalInfo":"","background":"","campaignName":"","icon":"","__typename":"pdpContentSnapshotThematicCampaign"},"stock":{"useStock":true,"value":"0","stockWording":"","__typename":"pdpContentSnapshotStock"},"variant":{"isVariant":true,"parentID":"1186331168","__typename":"pdpContentSnapshotVariant"},"wholesale":[],"isCashback":{"percentage":0,"__typename":"pdpContentSnapshotIsCashback"},"isTradeIn":false,"isOS":true,"isPowerMerchant":true,"isWishlist":false,"isCOD":false,"isFreeOngkir":{"isActive":false,"__typename":"pdpContentSnapshotFreeOngkir"},"preorder":{"duration":0,"timeUnit":"UNKNOWN","isActive":false,"preorderInDays":0,"__typename":"pdpContentSnapshotPreorder"},"__typename":"pdpDataProductContent","__typename":"pdpDataProductContent"}],"__typename":"pdpComponent"},{"name":"product_detail","type":"product_detail","position":"[1,2,1,1]","data":[{"content":[{"title":"Kondisi","subtitle":"Baru","applink":"","showAtFront":true,"isAnnotation":false,"__typename":"pdpContentProductDetail"},{"title":"Berat","subtitle":"7.000 Gram","applink":"","showAtFront":false,"isAnnotation":false,"__typename":"pdpContentProductDetail"},{"title":"Min. Pemesanan","subtitle":"1 Buah","applink":"","showAtFront":true,"isAnnotation":false,"__typename":"pdpContentProductDetail"},{"title":"Kategori","subtitle":"Laptop Gaming","applink":"https://www.tokopedia.com/p/komputer-laptop/pc-laptop-gaming/laptop-gaming","showAtFront":false,"isAnnotation":false,"__typename":"pdpContentProductDetail"},{"title":"Etalase","subtitle":"LAPTOP ASUS GAMING","applink":"https://www.tokopedia.com/agusidstoreapple/etalase/laptop-asus-gaming","showAtFront":true,"isAnnotation":false,"__typename":"pdpContentProductDetail"},{"title":"Deskripsi","subtitle":"Setiap pembelian unit di \u0026#34;AGUS ID STORE\u0026#34; Official Store\nCASHBACK HINGGA 400RB\n\nKLIK LINK DIBAWAH INI UNTUK UPGRADE RAM DAN PAKET INSTALL APLIKASI :)\n\nhttps://www.tokopedia.com/agusidstoreapple/etalase/paket-install-dan-upgrade-ram\n\nGRATIS BIAYA PEMASANGAN RAM\n\n\n⚠️Kenapa harus beli laptop di AGUS ID STORE ?\n\n- Produk kami 100% ORIGINAL\n- Uang kita kembalikan 2x lipat kalau barang tidak original\n- GARANSI RESMI Indonesia\n- BNIB (Brand New In Box) barang segel\n- Kami memiliki TEAM AFTERSALES buat bantu klaim garansi\n- Reseller / dropshipper are welcome\n\n📞 Fast Respon WA : *0821 2247 9856\n\nGARANSI:\n- Resmi Asus Indonesia 2 Tahun\n- Perfect Warranty (Accidental Damage Protection) 1 Tahun\n\nFREE: Asus Tuf Gaming Backpack selama persediaan masih ada\n\nMengenai varian:\nNon Bundle = Tidak dapat Bundling\nBundle MOUSE A Dapat Mouse paket A\nBundle HS A Dapat Headset paket A\nBundle MOUSE B Dapat Mouse paket B\nBundle HS B Headset paket B\nBundle MOUSE C Headset paket C\nBundle HS C Dapat Mouse paket C\nBundle MOUSE D Headset paket D\nBundle HS D Dapat Mouse paket D\nBundle M+H A Dapat Mouse \u0026amp; Headset Paket A\nBundle M+H B Dapat Mouse \u0026amp; Headset Paket B\nBundle M+H C Dapat Mouse \u0026amp; Headset Paket C\nBundle M+H D Dapat Mouse \u0026amp; Headset Paket D\nUNTUK PENJELASAN DETAILNYA ADA DISLIDE PRODUK\nBILA KURANG PAHAM BISA CHAT KE PRODUK KONSULTAN KAMI\n\n\nSPESIFIKASI PRODUK:\n- Prosesor : Intel® Core™ i5-10300H (Cache 8 M, hingga 4,50 GHz)\n- GPU : NVIDIA® GeForce® GTX 1650 4GB\n- Memory : 8GB DDR4\n- Storage : 512GB M.2 NVMe SSD\n- Display : 15.6 inch FHD 16:9 144Hz Value IPS-level\n- Resolusi : 1920 x 1080\n- OS : Windows 10 Home\n- Backlit Keyboard : Yes\n\nPORTS:\n1x Type A USB 2.0\n1x Type C USB 3.2 Gen 2\n2x Type A USB 3.2 Gen 1\n1x 3.5mm combo audio jack\t\t\n\n⚠️CEK ETALASE UNTUK LAPTOP DAN PRODUK KATEGORI LAINNYA: https://www.tokopedia.com/agusidstoreapple","applink":"","showAtFront":true,"isAnnotation":false,"__typename":"pdpContentProductDetail"},{"title":"Merek","subtitle":"ASUS","applink":"","showAtFront":false,"isAnnotation":true,"__typename":"pdpContentProductDetail"}],"__typename":"pdpDataProductDetail","__typename":"pdpDataProductDetail"}],"__typename":"pdpComponent"},{"name":"obat_keras","type":"custom_info","position":"[1,3,1,1]","data":[],"__typename":"pdpComponent"},{"name":"shop_credibility","type":"shop_credibility","position":"[1,4,1,1]","data":[],"__typename":"pdpComponent"},{"name":"shipment","type":"shipment","position":"[1,5,1,1]","data":[],"__typename":"pdpComponent"},{"name":"shipping","type":"info","position":"[1,6,1,1]","data":[{"icon":"","title":"Kurir","isApplink":true,"applink":"","content":[],"__typename":"pdpDataInfo","__typename":"pdpDataInfo"}],"__typename":"pdpComponent"},{"name":"shop_voucher","type":"shop_voucher","position":"[1,7,1,1]","data":[],"__typename":"pdpComponent"},{"name":"offerings","type":"offerings","position":"[1,8,1,1]","data":[],"__typename":"pdpComponent"},{"name":"installment_paylater","type":"info","position":"[1,9,1,1]","data":[{"icon":"https://ecs7.tokopedia.net/pdp/info/icon/pdp-paylatercicilan@3x.png","title":"Paylater \u0026 Cicilan","isApplink":true,"applink":"tokopedia://fintech/paylater?category=Laptop+Gaming\u0026price=13569000.000000\u0026productID=1186331168\u0026productURL=https%3A%2F%2Fwww.tokopedia.com%2Fagusidstoreapple%2Fasus-tuf-f15-fx506lh-i5-10300h-nvidia-gtx1650-144hz-8gb-512gb-ssd-w10","content":[],"__typename":"pdpDataInfo","__typename":"pdpDataInfo"}],"__typename":"pdpComponent"},{"name":"wholesale","type":"info","position":"[1,10,1,1]","data":[{"icon":"","title":"Harga Grosir","isApplink":true,"applink":"","content":[],"__typename":"pdpDataInfo","__typename":"pdpDataInfo"}],"__typename":"pdpComponent"},{"name":"protection","type":"info","position":"[1,11,1,1]","data":[{"icon":"https://ecs7.tokopedia.net/pdp/info/icon/pdp-protection@3x.png","title":"Proteksi Gadget","isApplink":false,"applink":"","content":[],"__typename":"pdpDataInfo","__typename":"pdpDataInfo"}],"__typename":"pdpComponent"},{"name":"report","type":"report","position":"[1,12,1,1]","data":[],"__typename":"pdpComponent"},{"name":"review","type":"review","position":"[0,13,2,1]","data":[],"__typename":"pdpComponent"},{"name":"tdn_topads","type":"banner_ads","position":"[0,14,2,1]","data":[],"__typename":"pdpComponent"},{"name":"discussion_faq","type":"discussion_faq","position":"[0,15,2,1]","data":[],"__typename":"pdpComponent"},{"name":"pdp_1","type":"product_list","position":"[0,16,3,1]","data":[],"__typename":"pdpComponent"},{"name":"pdp_2","type":"product_list","position":"[0,17,3,1]","data":[],"__typename":"pdpComponent"},{"name":"pdp_3","type":"product_list","position":"[0,18,3,1]","data":[],"__typename":"pdpComponent"},{"name":"pdp_4","type":"product_list","position":"[0,19,3,1]","data":[],"__typename":"pdpComponent"}],"__typename":"pdpLayout"}}}]
'''


# # item_description = "sinarmulia/lenovo-legion-5-pro-ryzen-7-5800h-rtx3060-1tb-ssd-16gb-16-wqxga-w10"
# # headers = {
# #     'authority': 'gql.tokopedia.com',
# #     'sec-ch-ua': '^\\^Chromium^\\^;v=^\\^92^\\^, ^\\^',
# #     'x-version': '27ca28b',
# #     'sec-ch-ua-mobile': '?0',
# #     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
# #     'content-type': 'application/json',
# #     'accept': '*/*',
# #     'x-source': 'tokopedia-lite',
# #     'x-device': 'desktop',
# #     'x-tkpd-lite-service': 'zeus',
# #     'x-tkpd-akamai': 'pdpGetLayout',
# #     'origin': 'https://www.tokopedia.com',
# #     'sec-fetch-site': 'same-site',
# #     'sec-fetch-mode': 'cors',
# #     'sec-fetch-dest': 'empty',
# #     'referer': f'https://www.tokopedia.com/{item_description}',
# #     'accept-language': 'en-US,en;q=0.9',
# #     'cookie': '_UUID_NONLOGIN_=5b7c1de52fea48e89a910249466603ce; hfv_banner=true; DID=e5e96033e209bae99614e829d2cffae1adfb797d7c79c5d2d5c229559e3fe9f02fe82ec0bec6d1bec406da00656d2e81; DID_JS=ZTVlOTYwMzNlMjA5YmFlOTk2MTRlODI5ZDJjZmZhZTFhZGZiNzk3ZDdjNzljNWQyZDVjMjI5NTU5ZTNmZTlmMDJmZTgyZWMwYmVjNmQxYmVjNDA2ZGEwMDY1NmQyZTgx47DEQpj8HBSa+/TImW+5JCeuQeRkm5NMpJWZG3hSuFU=; _gcl_au=1.1.819531658.1630065814; __auc=3d8e7d9317b877e7cdb86509d93; _jx=8133cb90-0731-11ec-badf-5db40e83e167; _fbp=fb.1.1630066980363.1866423534; RT=^\\^z=1&dm=tokopedia.com&si=4c09856f-224c-4b22-a7d5-63100921b85d&ss=kt0aa3oz&sl=1&tt=2a6&bcn=^%^2F^%^2F6852bd08.akstat.io^%^2F&nu=ehdzd6cbg&cl=2a4&ul=2a7&ld=2w6&hd=34o^\\^; _gid=GA1.2.231573036.1630548639; _SID_Tokopedia_=R5L8DvM23LNLDFYBKCF5VHPdlpEB0yN57WUf5tSQXQi5TCFXoJ7TL-RSzS5VgRlaoO3Of2toE1FSllgs5zsAdHjkUqfYk1tQIBA8k6fG0teB0pPo3fnStv9b6sbl1f8q; _CAS_=^%^7B^%^22dId^%^22^%^3A2166^%^2C^%^22aId^%^22^%^3A0^%^2C^%^22lbl^%^22^%^3A^%^22Andir^%^2C^%^20Kota^%^20Bandung^%^22^%^2C^%^22cId^%^22^%^3A165^%^2C^%^22long^%^22^%^3A^%^22^%^22^%^2C^%^22lat^%^22^%^3A^%^22^%^22^%^2C^%^22pCo^%^22^%^3A^%^22^%^22^%^2C^%^22wId^%^22^%^3A0^%^2C^%^22sId^%^22^%^3A11530573^%^7D; cto_bundle=SRmsh19vYllOSU8lMkYyR213NkZxJTJGeG9qMjlzTTg3OGlmZWZEbkpQMm8lMkJTdENkQW9hNnkyS3FFVzlXJTJGbjd5dE1IMjFHdEhqbzlrWnpoJTJGZDZsSlBKdFFoaEklMkJjYyUyRkk4NlhBeE5GVGhHMEZGbFRMaVRBMXVxV3JIZUc1NUlKRkNDRm9VdWYxU1NTVzFvS2NCaE1tellvOE50RGVYZyUzRCUzRA; _abck=CA8D568F68E76DD9EF69D38117C8DC19~0~YAAQ3fvOF7ZqGJt7AQAAOhDypwbJkmjGh2+PU+HCbVWXY71AKl2e4F8eauGwBJL38OJA2Ou4Kh4GU4Iwi6Oa46nj6uXrzQuV7yHXmsfZ8zSTluYOssiW5zWF3vfRkplr2dPrlxo4HEVT4Hgs+Ez2FVrbDRWmo2q+1P/RZh/e8lUwwZHxgBJiMoowhSu+eJ2bx/0rzhSeSMeMWYk6xqMDIqdQVsryF2iEc7T27/DXxnd+8JmPwb9IoMj11YY9NI5GE2qUfu9CJnlRDlRgSCv2mm1UswjyO1CKMBnUBlB6o+Dej5jr8vS4Cz9FyYgoitSCRhaOqbYyc4/k5bTANxNK9JhcTZMJz/a9u0b+sLjZgsdv3TrTsfNK604Ri7BYn9UL8PxL1X1ImzUpyT1UPaPn2Ly6X/mqPhOr6ZhU~-1~-1~-1; bm_sz=DA74DEF785268CAE6E5F42255B4CD658~YAAQ3fvOF7dqGJt7AQAAOxDypwyXRBiGh11xlHfDhm2htPMbRre3ymWXh98mk6t0RK+Cu/0BH2QXCaio4NB9SCDDzNAaL5o0oo3kEuxd7JQhWQLgyRl3e1lJKaaa9z9Go2AfIm9lJD2BQLoha8n8OFiEFC1yOOpd9OXFU9Tzlj3yvJllFvO1bmxoG6DJ2IwNbCmCdSrCfopSa94erKbag/l+chwPlVfOZ8FTCU28g8EEJjmIO4O4Y7/hr2mzzTHTdC+uBAueWZk1DTtDPwfETWcD8gQ3Zumd5rDFt84y7A+k23o4RPc=~4277571~3682610; _ga=GA1.2.817567506.1630065815; _dc_gtm_UA-9801603-1=1; _dc_gtm_UA-126956641-6=1; AMP_TOKEN=^%^24NOT_FOUND; _ga_70947XW48P=GS1.1.1630610265.12.0.1630610266.59',
# # }
# # shopDomain = item_description.split("/")[0]
# # productKey = item_description.split("/")[1]
# # payload = [
# #     {
# #         "operationName": "PDPGetLayoutQuery",
# #         "variables": {
# #             "shopDomain": shopDomain,
# #             "productKey": productKey,
# #             "layoutID": "",
# #             "apiVersion": 1,
# #             "userLocation": {
# #                 "addressID": "0",
# #                 "districtID": "2166",
# #                 "postalCode": "",
# #                 "latlon": ""
# #             }
# #         },
# #         "query": "fragment ProductVariant on pdpDataProductVariant {\n  errorCode\n  parentID\n  defaultChild\n  sizeChart\n  variants {\n    productVariantID\n    variantID\n    name\n    identifier\n    option {\n      picture {\n        urlOriginal: url\n        urlThumbnail: url100\n        __typename\n      }\n      productVariantOptionID\n      variantUnitValueID\n      value\n      hex\n      __typename\n    }\n    __typename\n  }\n  children {\n    productID\n    price\n    priceFmt\n    optionID\n    productName\n    productURL\n    picture {\n      urlOriginal: url\n      urlThumbnail: url100\n      __typename\n    }\n    stock {\n      stock\n      isBuyable\n      stockWording\n      stockWordingHTML\n      minimumOrder\n      maximumOrder\n      __typename\n    }\n    isCOD\n    isWishlist\n    campaignInfo {\n      campaignID\n      campaignType\n      campaignTypeName\n      campaignIdentifier\n      background\n      discountPercentage\n      originalPrice\n      discountPrice\n      stock\n      stockSoldPercentage\n      threshold\n      startDate\n      endDate\n      endDateUnix\n      appLinks\n      isAppsOnly\n      isActive\n      hideGimmick\n      isCheckImei\n      __typename\n    }\n    thematicCampaign {\n      additionalInfo\n      background\n      campaignName\n      icon\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment ProductMedia on pdpDataProductMedia {\n  media {\n    type\n    urlThumbnail: URLThumbnail\n    videoUrl: videoURLAndroid\n    prefix\n    suffix\n    description\n    __typename\n  }\n  videos {\n    source\n    url\n    __typename\n  }\n  __typename\n}\n\nfragment ProductHighlight on pdpDataProductContent {\n  name\n  price {\n    value\n    currency\n    __typename\n  }\n  campaign {\n    campaignID\n    campaignType\n    campaignTypeName\n    campaignIdentifier\n    background\n    percentageAmount\n    originalPrice\n    discountedPrice\n    originalStock\n    stock\n    stockSoldPercentage\n    threshold\n    startDate\n    endDate\n    endDateUnix\n    appLinks\n    isAppsOnly\n    isActive\n    hideGimmick\n    __typename\n  }\n  thematicCampaign {\n    additionalInfo\n    background\n    campaignName\n    icon\n    __typename\n  }\n  stock {\n    useStock\n    value\n    stockWording\n    __typename\n  }\n  variant {\n    isVariant\n    parentID\n    __typename\n  }\n  wholesale {\n    minQty\n    price {\n      value\n      currency\n      __typename\n    }\n    __typename\n  }\n  isCashback {\n    percentage\n    __typename\n  }\n  isTradeIn\n  isOS\n  isPowerMerchant\n  isWishlist\n  isCOD\n  isFreeOngkir {\n    isActive\n    __typename\n  }\n  preorder {\n    duration\n    timeUnit\n    isActive\n    preorderInDays\n    __typename\n  }\n  __typename\n}\n\nfragment ProductCustomInfo on pdpDataCustomInfo {\n  icon\n  title\n  isApplink\n  applink\n  separator\n  description\n  __typename\n}\n\nfragment ProductInfo on pdpDataProductInfo {\n  row\n  content {\n    title\n    subtitle\n    applink\n    __typename\n  }\n  __typename\n}\n\nfragment ProductDetail on pdpDataProductDetail {\n  content {\n    title\n    subtitle\n    applink\n    showAtFront\n    isAnnotation\n    __typename\n  }\n  __typename\n}\n\nfragment ProductDataInfo on pdpDataInfo {\n  icon\n  title\n  isApplink\n  applink\n  content {\n    icon\n    text\n    __typename\n  }\n  __typename\n}\n\nfragment ProductSocial on pdpDataSocialProof {\n  row\n  content {\n    icon\n    title\n    subtitle\n    applink\n    type\n    rating\n    __typename\n  }\n  __typename\n}\n\nquery PDPGetLayoutQuery($shopDomain: String, $productKey: String, $layoutID: String, $apiVersion: Float, $userLocation: pdpUserLocation!) {\n  pdpGetLayout(shopDomain: $shopDomain, productKey: $productKey, layoutID: $layoutID, apiVersion: $apiVersion, userLocation: $userLocation) {\n    name\n    pdpSession\n    basicInfo {\n      alias\n      id: productID\n      shopID\n      shopName\n      minOrder\n      maxOrder\n      weight\n      weightUnit\n      condition\n      status\n      url\n      needPrescription\n      catalogID\n      isLeasing\n      isBlacklisted\n      menu {\n        id\n        name\n        url\n        __typename\n      }\n      category {\n        id\n        name\n        title\n        breadcrumbURL\n        isAdult\n        detail {\n          id\n          name\n          breadcrumbURL\n          isAdult\n          __typename\n        }\n        __typename\n      }\n      blacklistMessage {\n        title\n        description\n        button\n        url\n        __typename\n      }\n      txStats {\n        transactionSuccess\n        transactionReject\n        countSold\n        paymentVerified\n        itemSoldPaymentVerified\n        __typename\n      }\n      stats {\n        countView\n        countReview\n        countTalk\n        rating\n        __typename\n      }\n      __typename\n    }\n    components {\n      name\n      type\n      position\n      data {\n        ...ProductMedia\n        ...ProductHighlight\n        ...ProductInfo\n        ...ProductDetail\n        ...ProductSocial\n        ...ProductDataInfo\n        ...ProductCustomInfo\n        ...ProductVariant\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n"
# #     }
# # ]
# #
# # api_key = "jJcauPNv4W2rg75x3tHGsbVqZAyLCpEY"
# # proxy_url = "http://falcon.proxyrotator.com:51337/?apiKey={}&userAgent=true&get=true".format(api_key)
# #
# #
# # def getProxy():
# #     try:
# #         r = requests.get(proxy_url, timeout=5)
# #         js = json.loads(r.text)
# #         # , js['randomUserAgent']
# #         return js['proxy']
# #     except Exception as e:
# #         pass
# #
# #
# # while True:
# #     try:
# #         proxy = getProxy()
# #         break
# #     except:
# #         pass
# #
# # while True:
# #     try:
# #         res = requests.post('https://gql.tokopedia.com/', headers=headers, json=payload, timeout=5,
# #                             proxies={'proxy': proxy})
# #         break
# #     except:
# #         pass
# #
# # products = json.loads(res.text[1:-1])
# # print(products)
#
# import requests
#
# session = requests.session()
#
# headers = {
#     'authority': 'gql.tokopedia.com',
#     'sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
#     'x-version': '7335090',
#     'sec-ch-ua-mobile': '?0',
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',
#     'content-type': 'application/json',
#     'accept': '*/*',
#     'x-source': 'tokopedia-lite',
#     'x-tkpd-lite-service': 'zeus',
#     'sec-ch-ua-platform': '"Windows"',
#     'origin': 'https://www.tokopedia.com',
#     'sec-fetch-site': 'same-site',
#     'sec-fetch-mode': 'cors',
#     'sec-fetch-dest': 'empty',
#     'referer': 'https://www.tokopedia.com/sinarmulia/lenovo-legion-5-pro-ryzen-7-5800h-rtx3060-1tb-ssd-16gb-16-wqxga-w10',
#     'accept-language': 'en-US,en;q=0.9',
# }
#
# data = '[{"operationName":"isAuthenticatedQuery","variables":{},"query":"query isAuthenticatedQuery {\\n  isAuthenticated\\n}\\n"}]'
#
# response = session.post('https://gql.tokopedia.com/', headers=headers, data=data)
#
# headers = {
#     'authority': 'gql.tokopedia.com',
#     'sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
#     'x-version': '7335090',
#     'sec-ch-ua-mobile': '?0',
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',
#     'content-type': 'application/json',
#     'accept': '*/*',
#     'x-source': 'tokopedia-lite',
#     'x-tkpd-lite-service': 'zeus',
#     'sec-ch-ua-platform': '"Windows"',
#     'origin': 'https://www.tokopedia.com',
#     'sec-fetch-site': 'same-site',
#     'sec-fetch-mode': 'cors',
#     'sec-fetch-dest': 'empty',
#     'referer': 'https://www.tokopedia.com/sinarmulia/lenovo-legion-5-pro-ryzen-7-5800h-rtx3060-1tb-ssd-16gb-16-wqxga-w10',
#     'accept-language': 'en-US,en;q=0.9',
# }
#
# data = '[{"operationName":"TrendingKeyword","variables":{},"query":"query TrendingKeyword {\\n  trending_keywords {\\n    keywords {\\n      url\\n      keyword\\n      __typename\\n    }\\n    __typename\\n  }\\n}\\n"}]'
#
# response = session.post('https://gql.tokopedia.com/', headers=headers, data=data)
#
# headers = {
#     'authority': 'gql.tokopedia.com',
#     'sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
#     'x-version': '7335090',
#     'sec-ch-ua-mobile': '?0',
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',
#     'content-type': 'application/json',
#     'accept': '*/*',
#     'x-source': 'tokopedia-lite',
#     'queryhash': 'v1:71b3e927ca1c0c03fe18550f581ac3e8;false',
#     'x-tkpd-lite-service': 'zeus',
#     'sec-ch-ua-platform': '"Windows"',
#     'origin': 'https://www.tokopedia.com',
#     'sec-fetch-site': 'same-site',
#     'sec-fetch-mode': 'cors',
#     'sec-fetch-dest': 'empty',
#     'referer': 'https://www.tokopedia.com/sinarmulia/lenovo-legion-5-pro-ryzen-7-5800h-rtx3060-1tb-ssd-16gb-16-wqxga-w10',
#     'accept-language': 'en-US,en;q=0.9',
# }
#
# data = {
#   '[{"operationName":"RolloutFeatureVariants","variables":{"rev":0,"client_id":4,"iris_session_id":"d3d3LnRva29wZWRpYS5jb20': '.a2b0c5d362f3845ca9d317452699f702.1635627488590","id":"c3aa77d3088e3dca66f55f77b4d2aa4f"}}]'
# }
#
# reqq = session.post('https://gql.tokopedia.com/', headers=headers, data=data)
#
#
# headers = {
#     'authority': 'gql.tokopedia.com',
#     'sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
#     'tkpd-userid': '0',
#     'sec-ch-ua-mobile': '?0',
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',
#     'content-type': 'application/json',
#     'accept': '*/*',
#     'x-version': '7335090',
#     'x-source': 'tokopedia-lite',
#     'x-device': 'desktop',
#     'x-tkpd-lite-service': 'zeus',
#     'sec-ch-ua-platform': '"Windows"',
#     'origin': 'https://www.tokopedia.com',
#     'sec-fetch-site': 'same-site',
#     'sec-fetch-mode': 'cors',
#     'sec-fetch-dest': 'empty',
#     'referer': 'https://www.tokopedia.com/sinarmulia/lenovo-legion-5-pro-ryzen-7-5800h-rtx3060-1tb-ssd-16gb-16-wqxga-w10',
#     'accept-language': 'en-US,en;q=0.9',
# }
#
# data = '[{"operationName":"dynamicPlaceHolder","variables":{"navsource":"home","unique_id":"c3aa77d3088e3dca66f55f77b4d2aa4f"},"query":"query dynamicPlaceHolder($navSource: String!, $unique_id: String) {\\n  universe_placeholder(navsource: $navSource, unique_id: $unique_id) {\\n    data {\\n      keyword\\n      placeholder\\n      __typename\\n    }\\n    __typename\\n  }\\n}\\n"}]'
#
# response = session.post('https://gql.tokopedia.com/', headers=headers, data=data)
#
#
#
#
#
# headers = {
#     'authority': 'gql.tokopedia.com',
#     'sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
#     'x-version': '7335090',
#     'sec-ch-ua-mobile': '?0',
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',
#     'content-type': 'application/json',
#     'accept': '*/*',
#     'x-tkpd-akamai': 'pdpGetLayout',
#     'x-source': 'tokopedia-lite',
#     'x-device': 'desktop',
#     'x-tkpd-lite-service': 'zeus',
#     'sec-ch-ua-platform': '"Windows"',
#     'origin': 'https://www.tokopedia.com',
#     'sec-fetch-site': 'same-site',
#     'sec-fetch-mode': 'cors',
#     'sec-fetch-dest': 'empty',
#     'referer': 'https://www.tokopedia.com/sinarmulia/lenovo-legion-5-pro-ryzen-7-5800h-rtx3060-1tb-ssd-16gb-16-wqxga-w10',
#     'accept-language': 'en-US,en;q=0.9',
#     'cookie': '_UUID_NONLOGIN_=c3aa77d3088e3dca66f55f77b4d2aa4f; _UUID_NONLOGIN_.sig=OnXO11KwJRJAXpiArXyAsYf-4q4; DID=1e310bf694d656972f8e25438dd662cc0f18672e6e3530724f7c3011f2bf57fa51aedbdedc33295314dc7174d48c62f4; DID_JS=MWUzMTBiZjY5NGQ2NTY5NzJmOGUyNTQzOGRkNjYyY2MwZjE4NjcyZTZlMzUzMDcyNGY3YzMwMTFmMmJmNTdmYTUxYWVkYmRlZGMzMzI5NTMxNGRjNzE3NGQ0OGM2MmY047DEQpj8HBSa+/TImW+5JCeuQeRkm5NMpJWZG3hSuFU=; _gcl_au=1.1.1236403990.1633658718; __auc=301e35ba17c5da5d8b1421fefdf; _fbp=fb.1.1633658724009.1874031859; _jx=3318bb70-27dc-11ec-98a1-4529a537d922; bm_sz=0B6F022D34357D0BF643DAFA16DC48D3~YAAQRcETAmM0G598AQAAvM3+0g2EHlAZ8sgJgR0SWJo7/IRSSiKeI04XDrAth3OqW83i+8+uGh5VX4zuD9MeT3VDSxZ7q2VmCN1ZfjtpUncYec2aY+9v+3DK1xb5GipzfkaZsct3ZEqnhodHDsJ0F+41luymuylAaZs+FV1mjx6NHCfo6wp8bwCT9AaGyzNBrOEbR3pDzxCuejrqG7WGxFcyTjMkEWHvfRn2S1DYl2jOYc7ZzQgpNjWR+1tRSIPHM46lmpFbTyKRzlmv/ip4fBSVcyBoQMTvJ5LYzq1oJIYy4g0xsPI=~4272436~4539440; _gid=GA1.2.2016662179.1635627488; _SID_Tokopedia_=5g0TYssV_ACfdBgbvgdBukT4VUt0Iqch8P2DuRilMEPMLOGDxDM3MReC4EmI7pni1mnVsoqkRmFH8tZHxWptfEHE1Wik8E7jzQ6Gkn8GIk8Hkm12iXKQ3TRM7HxTT2WR; AMP_TOKEN=%24NOT_FOUND; __asc=6bf7044e17cd2fee8175dea3ba5; ak_bmsc=31D29DBCA08DA5421187070EEB43F1CB~000000000000000000000000000000~YAAQRcETAnw0G598AQAAoOj+0g0MMBB1kyl5ARw3Y4/YXqCtpFNSMzx6yBQMtr4y94saQpYjHkSDZy/b53Lw/DkoS+7g+jQsWO8/k9WCAAmsUh0jivDbtLTWNn8RKtxLfL+DVHixB+aHuKZCscIEJa9Kb75g7X/bRz2tYcfQBmr9fAkxH+06QFmYftqJK5KgMYIrkcj9ZH4WxdlHPaaOnXDKFHRU5CzlGxMwuvKFV5MlJGQo0HmRui0dVLu3OGPPusclsXKua9040qN7FV1gbCCQTRpY8vbLWgIYQR5Z5Qf4IkcCK1I401aBg+UdbeFFGbjvFTO4dBnF0y0AdFNeXnCvwwhUO9wrO0mx+b4F7TOQXWTVhvjNoD2UqDRUB4iSk8jh9qefIxd5dxARnw==; _jxs=1635627496-3318bb70-27dc-11ec-98a1-4529a537d922; bm_sv=14817EF4BFCE1BBC44F2681333D39BFC~s7LFaGOL/ZOelyDwbCb7kQ7ENvhTeUl6W2JhREoqgrS9MFp47AH3ZyfuMEBb0oDkeEb/iMXuHgZ1tWN1hdOiy+S0KOdd4dpM5TyYv2VvWO2b3KQM3Hb8qBUhcFQQefwkqoc3SfsyBKbfr+bxiRbjxAmwO50Szu+4UkEcAW1g494=; _gat_UA-9801603-1=1; cto_bundle=DCAQLl96M0FjUGUlMkZzQk16ZWhteThiNXhkVkt2SEtzR3Z4dXh1a0xIQXdWdnMwUENEc2xmY3BBUSUyQjFMalEzOSUyQnVUVWolMkZCNjVLZGlJVVFJSHQxMlFObk5jUHh5YXpDS2ZiTiUyRmtIUVl3Z1RkUEhCRGdHUXdndWJFaHVtVGFuSGJWJTJCMVpjaFNFcXAzbkVHekt5eGF0NnZQQnVkUUElM0QlM0Q; _ga_70947XW48P=GS1.1.1635627487.4.1.1635627560.60; _abck=90A04B84E4689C43040204F2D24ADD2E~0~YAAQRcETApM3G598AQAAmu//0gZE48urDg5AaJCEFRcJ/u/wtelpYKuF5np2CpYPu88ufBHMy1GHXSi0vlXA5Asj/avOSHZWWA1H7CfpL4xwcNZ0/QE8xhNDQ3fi6pYAfGQrsH3ZedHs+xlQ68gUJ00uedw+wzeUNZadUkrKEh/zcD3a4IQibeXzTNHM4jzRKMMNEG1o1VUcwra/JUik7wG5k/RiNYy2C3qriUB4oDoTOqCNdG/7XIgxSEF5da6kGjKR4TpuNeYhzFAF1FexVRXmWoFcGXrar0qu9h5Q4gbTbSdlQlmPwkxNHAdqw7I60pbgrW1agLLAt8fzRjFZER+ntxNiauZyYSukUshlCNDHzUD1yShCh1tIYF4w4NgoVYXmLB1N6t1XMInwn2hgctTnQAaj1hsb5ArD~-1~-1~-1; _ga=GA1.2.655637166.1633658718; _dc_gtm_UA-126956641-6=1; _dc_gtm_UA-9801603-1=1',
# }
# data = '[{"operationName":"PDPGetLayoutQuery","variables":{"shopDomain":"sinarmulia","productKey":"lenovo-legion-5-pro-ryzen-7-5800h-rtx3060-1tb-ssd-16gb-16-wqxga-w10","layoutID":"","apiVersion":1,"userLocation":{"addressID":"0","districtID":"2274","postalCode":"","latlon":""}},"query":"fragment ProductVariant on pdpDataProductVariant {\\n  errorCode\\n  parentID\\n  defaultChild\\n  sizeChart\\n  variants {\\n    productVariantID\\n    variantID\\n    name\\n    identifier\\n    option {\\n      picture {\\n        urlOriginal: url\\n        urlThumbnail: url100\\n        __typename\\n      }\\n      productVariantOptionID\\n      variantUnitValueID\\n      value\\n      hex\\n      __typename\\n    }\\n    __typename\\n  }\\n  children {\\n    productID\\n    price\\n    priceFmt\\n    optionID\\n    productName\\n    productURL\\n    picture {\\n      urlOriginal: url\\n      urlThumbnail: url100\\n      __typename\\n    }\\n    stock {\\n      stock\\n      isBuyable\\n      stockWordingHTML\\n      minimumOrder\\n      maximumOrder\\n      __typename\\n    }\\n    isCOD\\n    isWishlist\\n    campaignInfo {\\n      campaignID\\n      campaignType\\n      campaignTypeName\\n      campaignIdentifier\\n      background\\n      discountPercentage\\n      originalPrice\\n      discountPrice\\n      stock\\n      stockSoldPercentage\\n      startDate\\n      endDate\\n      endDateUnix\\n      appLinks\\n      isAppsOnly\\n      isActive\\n      hideGimmick\\n      isCheckImei\\n      __typename\\n    }\\n    thematicCampaign {\\n      additionalInfo\\n      background\\n      campaignName\\n      icon\\n      __typename\\n    }\\n    __typename\\n  }\\n  __typename\\n}\\n\\nfragment ProductMedia on pdpDataProductMedia {\\n  media {\\n    type\\n    urlThumbnail: URLThumbnail\\n    videoUrl: videoURLAndroid\\n    prefix\\n    suffix\\n    description\\n    __typename\\n  }\\n  videos {\\n    source\\n    url\\n    __typename\\n  }\\n  __typename\\n}\\n\\nfragment ProductHighlight on pdpDataProductContent {\\n  name\\n  price {\\n    value\\n    currency\\n    __typename\\n  }\\n  campaign {\\n    campaignID\\n    campaignType\\n    campaignTypeName\\n    campaignIdentifier\\n    background\\n    percentageAmount\\n    originalPrice\\n    discountedPrice\\n    originalStock\\n    stock\\n    stockSoldPercentage\\n    threshold\\n    startDate\\n    endDate\\n    endDateUnix\\n    appLinks\\n    isAppsOnly\\n    isActive\\n    hideGimmick\\n    __typename\\n  }\\n  thematicCampaign {\\n    additionalInfo\\n    background\\n    campaignName\\n    icon\\n    __typename\\n  }\\n  stock {\\n    useStock\\n    value\\n    stockWording\\n    __typename\\n  }\\n  variant {\\n    isVariant\\n    parentID\\n    __typename\\n  }\\n  wholesale {\\n    minQty\\n    price {\\n      value\\n      currency\\n      __typename\\n    }\\n    __typename\\n  }\\n  isCashback {\\n    percentage\\n    __typename\\n  }\\n  isTradeIn\\n  isOS\\n  isPowerMerchant\\n  isWishlist\\n  isCOD\\n  isFreeOngkir {\\n    isActive\\n    __typename\\n  }\\n  preorder {\\n    duration\\n    timeUnit\\n    isActive\\n    preorderInDays\\n    __typename\\n  }\\n  __typename\\n}\\n\\nfragment ProductCustomInfo on pdpDataCustomInfo {\\n  icon\\n  title\\n  isApplink\\n  applink\\n  separator\\n  description\\n  __typename\\n}\\n\\nfragment ProductInfo on pdpDataProductInfo {\\n  row\\n  content {\\n    title\\n    subtitle\\n    applink\\n    __typename\\n  }\\n  __typename\\n}\\n\\nfragment ProductDetail on pdpDataProductDetail {\\n  content {\\n    title\\n    subtitle\\n    applink\\n    showAtFront\\n    isAnnotation\\n    __typename\\n  }\\n  __typename\\n}\\n\\nfragment ProductDataInfo on pdpDataInfo {\\n  icon\\n  title\\n  isApplink\\n  applink\\n  content {\\n    icon\\n    text\\n    __typename\\n  }\\n  __typename\\n}\\n\\nfragment ProductSocial on pdpDataSocialProof {\\n  row\\n  content {\\n    icon\\n    title\\n    subtitle\\n    applink\\n    type\\n    rating\\n    __typename\\n  }\\n  __typename\\n}\\n\\nquery PDPGetLayoutQuery($shopDomain: String, $productKey: String, $layoutID: String, $apiVersion: Float, $userLocation: pdpUserLocation!) {\\n  pdpGetLayout(shopDomain: $shopDomain, productKey: $productKey, layoutID: $layoutID, apiVersion: $apiVersion, userLocation: $userLocation) {\\n    name\\n    pdpSession\\n    basicInfo {\\n      alias\\n      isQA\\n      id: productID\\n      shopID\\n      shopName\\n      minOrder\\n      maxOrder\\n      weight\\n      weightUnit\\n      condition\\n      status\\n      url\\n      needPrescription\\n      catalogID\\n      isLeasing\\n      isBlacklisted\\n      menu {\\n        id\\n        name\\n        url\\n        __typename\\n      }\\n      category {\\n        id\\n        name\\n        title\\n        breadcrumbURL\\n        isAdult\\n        detail {\\n          id\\n          name\\n          breadcrumbURL\\n          isAdult\\n          __typename\\n        }\\n        __typename\\n      }\\n      txStats {\\n        transactionSuccess\\n        transactionReject\\n        countSold\\n        paymentVerified\\n        itemSoldPaymentVerified\\n        __typename\\n      }\\n      stats {\\n        countView\\n        countReview\\n        countTalk\\n        rating\\n        __typename\\n      }\\n      __typename\\n    }\\n    components {\\n      name\\n      type\\n      position\\n      data {\\n        ...ProductMedia\\n        ...ProductHighlight\\n        ...ProductInfo\\n        ...ProductDetail\\n        ...ProductSocial\\n        ...ProductDataInfo\\n        ...ProductCustomInfo\\n        ...ProductVariant\\n        __typename\\n      }\\n      __typename\\n    }\\n    __typename\\n  }\\n}\\n"}]'
#
# response = session.post('https://gql.tokopedia.com/', headers=headers, data=data)
# print(response.text)
# input()
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# https://www.tokopedia.com/sinarmulia/lenovo-legion-5-pro-ryzen-7-5800h-rtx3060-1tb-ssd-16gb-16-wqxga-w10
#
# #vec 1
# _abck=90A04B84E4689C43040204F2D24ADD2E~0~YAAQRcETAq83G598AQAAU/b/0gav2BAeuxhJ4WghcfXisTswr07DqlwfS+FRxu0GMA4cU95BhcCznc0vusAQ+KNSkMSxYgde2iX1CvO4XPAzSPkbRfAHmKUrX0r8YpIQSaswNvtDOagbUhq8ZkkPqTvbksah9vfSA2coJJJE9rK+uG9gneqhuYtuleYri3nTIygy3DnWWmkfY+ITRdCnINQhFT+VUQTB6iE7bNmVjkTq01mEk6EOoOTdhwwfC11QeLe0tlk7eAREw+AWoAns1niVYGhMHj1gnUq4N7UcuUqlo8ZkHChsWcDvmdJbBsHAZeRvdbFYXN59Ox5CVRDYawoXm7UpWtw8b3Mw/ObFKd+OQY9EXiumK8Vy6VQReg3fsjzUCNoA1ypw+4G8y3tVW4tghEW3h3A/kNi1~-1~-1~-1;
# cto_bundle=r-5Zfl96M0FjUGUlMkZzQk16ZWhteThiNXhkVkVUeGpyUDVZJTJCOFN3ckcxNEZOZklVajcxcVRoNnZGRGQ0MzVvUWFsZElMT01pYVBEbjN1blZpcWpjU0ZnWGtxZ0dpbTBseWNXRiUyRiUyRnJDc3Z3VDVUd2o5cWl2WDFMU3JHTlpjNjlLZ2JKNUpQSG4yc2dMZTJwUnJPak9NcCUyRkxYJTJCdnclM0QlM0Q;
# _ga_70947XW48P=GS1.1.1635630247.5.0.1635630247.60;
#
# #vec 2
# _abck=90A04B84E4689C43040204F2D24ADD2E~0~YAAQTMETAlzdLVZ8AQAAm/Yo0wbCbCRF4oC5ZvN2IVsfn3cKVJK08wqukGCa5xx0p5yZPquAuW2p3K+TZz5QWVPZwMI5FlVNC9FH4f9HXglMhpqhmt9ZXQeipRjnYgfd7dpRm5aFMuUt5MMTLPfumDAXUq1caQSbcno8GJJMkS4Y+WzbbxsD/BsA4qu1UW2iud7/yLp4Chc0CCSetXc3faYsVNBpONXE2SYw/VZIQXol3Vl62EiKkce3lA0x2YhY9q6uQdPy2TpNE+DijukF8RvlEjCF23aw3+JSr/fT01IS4M2yJqWZARTmpSYNCiJ8Y9SPFB4H2BYswXXoqPvnyec+yEBfW1rEMjd2YllkVM8mV+/KdPkEFWSTHiN7ErcaLhHq4XXECyirCWbHXRwJUh6CNqrcuhYToltl~-1~-1~-1;
# __asc=2cc3af7917cd329028ce3bb9e3d;
# cto_bundle=Ea968l96M0FjUGUlMkZzQk16ZWhteThiNXhkVklGZ29PMW1OQmZpNHVIbW1JUGZBSXJDcjRVeEF2R05FRWFNbFpldFRqNkJrRklPM3VMVjZLRGRwSld2bElLRTlsRjBiYXljbW9uT0olMkJkdGRDMWxMd2NWd0FPZEtHYU9KdnpBWXNKYzQ2d0k0OGdibE1VNkJTbTNSUnBFVDBTRlZRJTNEJTNE;
# _ga_70947XW48P=GS1.1.1635630247.5.1.1635631040.60;
# _jxs=1635630256-3318bb70-27dc-11ec-98a1-4529a537d922;
#
#
#
#
#
#
#
# #perbashket
# _UUID_NONLOGIN_=c3aa77d3088e3dca66f55f77b4d2aa4f; _UUID_NONLOGIN_.sig=OnXO11KwJRJAXpiArXyAsYf-4q4; DID=1e310bf694d656972f8e25438dd662cc0f18672e6e3530724f7c3011f2bf57fa51aedbdedc33295314dc7174d48c62f4; DID_JS=MWUzMTBiZjY5NGQ2NTY5NzJmOGUyNTQzOGRkNjYyY2MwZjE4NjcyZTZlMzUzMDcyNGY3YzMwMTFmMmJmNTdmYTUxYWVkYmRlZGMzMzI5NTMxNGRjNzE3NGQ0OGM2MmY047DEQpj8HBSa+/TImW+5JCeuQeRkm5NMpJWZG3hSuFU=; _gcl_au=1.1.1236403990.1633658718; __auc=301e35ba17c5da5d8b1421fefdf; _fbp=fb.1.1633658724009.1874031859; _jx=3318bb70-27dc-11ec-98a1-4529a537d922; bm_sz=0B6F022D34357D0BF643DAFA16DC48D3~YAAQRcETAmM0G598AQAAvM3+0g2EHlAZ8sgJgR0SWJo7/IRSSiKeI04XDrAth3OqW83i+8+uGh5VX4zuD9MeT3VDSxZ7q2VmCN1ZfjtpUncYec2aY+9v+3DK1xb5GipzfkaZsct3ZEqnhodHDsJ0F+41luymuylAaZs+FV1mjx6NHCfo6wp8bwCT9AaGyzNBrOEbR3pDzxCuejrqG7WGxFcyTjMkEWHvfRn2S1DYl2jOYc7ZzQgpNjWR+1tRSIPHM46lmpFbTyKRzlmv/ip4fBSVcyBoQMTvJ5LYzq1oJIYy4g0xsPI=~4272436~4539440; _gid=GA1.2.2016662179.1635627488; _SID_Tokopedia_=5g0TYssV_ACfdBgbvgdBukT4VUt0Iqch8P2DuRilMEPMLOGDxDM3MReC4EmI7pni1mnVsoqkRmFH8tZHxWptfEHE1Wik8E7jzQ6Gkn8GIk8Hkm12iXKQ3TRM7HxTT2WR; AMP_TOKEN=$NOT_FOUND; ak_bmsc=31D29DBCA08DA5421187070EEB43F1CB~000000000000000000000000000000~YAAQRcETAnw0G598AQAAoOj+0g0MMBB1kyl5ARw3Y4/YXqCtpFNSMzx6yBQMtr4y94saQpYjHkSDZy/b53Lw/DkoS+7g+jQsWO8/k9WCAAmsUh0jivDbtLTWNn8RKtxLfL+DVHixB+aHuKZCscIEJa9Kb75g7X/bRz2tYcfQBmr9fAkxH+06QFmYftqJK5KgMYIrkcj9ZH4WxdlHPaaOnXDKFHRU5CzlGxMwuvKFV5MlJGQo0HmRui0dVLu3OGPPusclsXKua9040qN7FV1gbCCQTRpY8vbLWgIYQR5Z5Qf4IkcCK1I401aBg+UdbeFFGbjvFTO4dBnF0y0AdFNeXnCvwwhUO9wrO0mx+b4F7TOQXWTVhvjNoD2UqDRUB4iSk8jh9qefIxd5dxARnw==; bm_sv=14817EF4BFCE1BBC44F2681333D39BFC~s7LFaGOL/ZOelyDwbCb7kQ7ENvhTeUl6W2JhREoqgrS9MFp47AH3ZyfuMEBb0oDkeEb/iMXuHgZ1tWN1hdOiy+S0KOdd4dpM5TyYv2VvWO2b3KQM3Hb8qBUhcFQQefwkqoc3SfsyBKbfr+bxiRbjxAmwO50Szu+4UkEcAW1g494=;
# _dc_gtm_UA-126956641-6=1;
# _dc_gtm_UA-9801603-1=1
# _ga=GA1.2.655637166.1633658718;