from os import getenv

class Worken:

    def __init__(self) -> None:
        self.__contractAddress = "0x3AE0726b5155fCa70dd79C0839B07508Ce7F0F13"
        self.__nodeUrl = "https://rpc-mumbai.maticvigil.com/"
        self.__apiKey = getenv("WORKEN_POLYGONSCAN_APIKEY")
        self.__web3 = Web3(Web3.HTTPProvider(self.__nodeUrl))
        self.__wallet = "0xf68A2B061c1aFC3ed07FafF33c53978F80F54099"