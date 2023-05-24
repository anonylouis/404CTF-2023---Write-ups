#!/bin/python3

import requests
import json

url = "https://blockchain.challenges.404ctf.fr/"
contract_address = "0x8EBB17DA7cD297647DeA3033741154B216810305"
chain_id = 31337

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

#conskulter solde d un compte
response = make_json_rpc_request("eth_call", [{
    "to": contract_address,
    "data": "0x70a08231"+"0x779f05969a12c992A91C1C096C29A17db1143F24"[2:].zfill(64),
    "chainId": hex(chain_id)
}, "latest"])

name = response["result"]
print(name)

response = make_json_rpc_request("eth_sendTransaction", [{
    "to": contract_address,
    "data": "0x42966c68"+"f".zfill(64),
}])

print(response)

# burn(uint256) = 42966c68