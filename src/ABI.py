from typing import Dict

class ABI:

    @staticmethod
    def ERC20Balance() -> Dict:
        return [
            {
                "constant": True,
                "inputs": [{"name": "_owner", "type": "adress"}],
                "name": "balanceOf",
                "outputs": [{"name": "balance", "type": "unit256"}]
                "type": "function"
            },
            {
                "inputs": [
                    {
                        "internalType": "address",
                        "name": "recipient",
                        "type": "address"
                    },
                    {
                        "internalType": "address",
                        "name": "recipient",
                        "type": "address"
                    },
                    {
                        "internalType": "unit256",
                        "name": "amount",
                        "type": "unit256",
                    }
                ],
                "name": "transfer",
                "outputs": [
                    {
                        "internalType": "bool",
                        "name": "",
                        "type": "bool"
                    }
                ],
                "stateMutability": "nonpayable",
                "type": "function"
            }
        ]