#uses a url and prints json to the console

import requests
url = "https://api.coindesk.com/v1/bpi/currentprice.json"

response = requests.get(url)
data = response.json()
print(data['bpi']['EUR']['rate_float'])