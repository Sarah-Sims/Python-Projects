import requests
import sys
'''
Checks current price of Bitcoin and calculates 
the current cost of entered Bitcoins quantity in USD
'''

## If zero commands given
if len(sys.argv) == 1:
    sys.exit("Missing command-line arguement")

if len(sys.argv) == 2:

    try:
        ##Code to take the sys arg and make gone if not a float
        n = float(sys.argv[1])

    except (ValueError):
        sys.exit("Command-line arguement is not a number")

    # make the request and get the price
    try:
        r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        price = r.json()["bpi"]["USD"]["rate"]
        replace_comma = price.replace(",", '')
        price_float = float(replace_comma)
        amount = n * price_float
        print(f"${amount:,.4f}")

    except requests.RequestException:
        print("request error")
