import requests
from web3 import Web3
from typing import Dict
import json

endpoint = "https://api-testnet.polygonscan.com/api?module=contract&action=getabi&address=0x50802059B3A299b36bc2c71aBEDBA450032f49AB&apikey=YourApiKeyToken"

response = requests.get(endpoint)
data = response.json()
print(data)