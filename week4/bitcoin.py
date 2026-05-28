import sys
import requests

try:
    quantity = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")
except IndexError:
    sys.exit("Missing command-line argument ")


bitrequest = requests.get('https://rest.coincap.io/v3/assets/bitcoin?apiKey=a545756cbf472c5b119c08464fe1a25b6b9502594b30adb2445aa6d46981ff35')
bitrequest = bitrequest.json()


bitprice = float(bitrequest['data']['priceUsd'])
#bitrequest.get('data',{}).get('priceUsd', None)

pricetopay = bitprice * quantity

print(f'${pricetopay:,.4f}')