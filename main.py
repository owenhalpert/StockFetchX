import urllib.parse
import requests

main_api = "https://stockx.com/api/products/"

##sku will be user set, placeholder for now
sku =  'adidas-yeezy-boost-350-v2-white-core-black-red?includes=market,360'
url = main_api + urllib.parse.urlencode({'sku': sku})

json_data = requests.get(url).json()
print(json_data)

#need to format printed data 
#3 to 2.7
