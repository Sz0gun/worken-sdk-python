import requests
from web3 import Web3
from ..utils.ABI import ABI
from typing import Dict


endpoint = "https://api-testnet.polygonscan.com/api?module=contract&action=getabi&address=0x50802059B3A299b36bc2c71aBEDBA450032f49AB&apikey=YourApiKeyToken"

def getBalance(web3: Web3, contract_address: str) -> Dict:
    web = web3
    contract = web3.eth.contract(adress=contract_address, abi=ABI.ERC20Balance())

    return contract.functions.balance0f(address).call()

getBalance(endpoint)