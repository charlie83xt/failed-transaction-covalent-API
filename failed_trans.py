import requests
import json
from urllib.parse import urljoin

# Forms the requests url after address and key input from user
COVALENT = 'https://api.covalenthq.com/v1/1/address/'
address = input('Address:')
url1 = COVALENT + address 
url2 = url1 + '/transactions_v2/?key='
api_key = input('Key:')
url3 = url2 + api_key
url = url3 + '/&primer={"$match":{"successful": false}}'

response = requests.get(url)

# Response is loaded and printed in console
data = json.loads(response.text)
print(data)
print(url)