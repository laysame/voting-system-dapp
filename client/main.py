import sys
import web3
from web3 import Web3, eth

w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))

if not w3.is_connected():
    print("Ganache not connected")
    sys.exit(1)

caller = "0xf43993E8D11c7BDf222360042797682FB630F41e"
private_key = "694d40ea85bbe17b9c5dd1f4034cd92009127fc5fb3665038bcc5f64e6834da2"

contract_address = "0x43f81b677C9CAD64cB3449b57C27D3301c848f43"

contract_abi = """[
  {
    "anonymous": false,
    "inputs": [
      {
        "indexed": true,
        "internalType": "uint256",
        "name": "_candidateId",
        "type": "uint256"
      }
    ],
    "name": "votedEvent",
    "type": "event"
  },
  {
    "inputs": [],
    "name": "election",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "uint256",
        "name": "_candidateId",
        "type": "uint256"
      }
    ],
    "name": "vote",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "name": "candidates",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "id",
        "type": "uint256"
      },
      {
        "internalType": "string",
        "name": "name",
        "type": "string"
      },
      {
        "internalType": "uint256",
        "name": "voteCount",
        "type": "uint256"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "candidatesCount",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "",
        "type": "address"
      }
    ],
    "name": "voters",
    "outputs": [
      {
        "internalType": "bool",
        "name": "",
        "type": "bool"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  }
]"""

contract = w3.eth.contract(address=contract_address, abi=contract_abi)
nonce = w3.eth.get_transaction_count(caller)

call_function_tx = contract.functions.vote(1).build_transaction(
    {
        "chainId": w3.eth.chain_id,
        "gasPrice": w3.eth.gas_price,
        "from": caller,
        "nonce": nonce,
    }
)

signed_tx = w3.eth.account.sign_transaction(call_function_tx, private_key=private_key)
send_tx = w3.eth.send_raw_transaction(signed_tx.rawTransaction)

tx_receipt = w3.eth.wait_for_transaction_receipt(send_tx)
print(tx_receipt)
