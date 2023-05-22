#!/bin/python3
import requests
import json

import requests
import json

url = "https://blockchain.challenges.404ctf.fr/"
chain_id = 31337
contract_address = "0x053012A242d8Bf0E4C008BFA44bf3768195F2284"

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

import hashlib

def generate_function_selector(signature):
    # Supprimez les espaces blancs et les types de données de la signature
    signature = signature.replace(" ", "").split("(")[0]

    # Calculez l'hash SHA3-256 de la signature
    signature_hash = hashlib.sha3_256(signature.encode()).hexdigest()

    # Prenez les 4 premiers octets de l'hash pour obtenir le sélecteur de fonction
    function_selector = signature_hash[:8]

    return "0x" + function_selector

# Utilisez la signature de la fonction guess pour générer le sélecteur de fonction
guess_signature = "guess(uint256)"
guess_function_selector = generate_function_selector(guess_signature)
print(guess_function_selector)

# Exemple d'appel à la méthode "guess" avec l'adresse du contrat et les paramètres requis
next_value = 42
response = make_json_rpc_request("eth_sendTransaction", [{
    "to": contract_address,
    "data": "0x52c84dce" + "000000000000000000000000000000000000000000000000000000000000002a",
    "chainId": hex(chain_id)
}])
print(response)