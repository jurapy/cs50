import sys
import requests
import json

if not len(sys.argv) == 2:
    sys.exit('Missing command-line argument')

try:
    number = float(sys.argv[1])
except ValueError:
    sys.exit('Command-line argument is not a number')

get = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')

bitjson = get.json()

bitcoin = bitjson['bpi']['USD']['rate_float']

print(f'${bitcoin * number:,.4f}')
