#!/bin/python3

from Cryptodome.Cipher import AES

# Clé
key = bytes.fromhex("00456c6c616e61206427416c2d466172")

# Nonce
nonce = bytes.fromhex("00")

# Message chiffré
ciphertext = bytes.fromhex("ac6679386ffcc3f82d6fec9556202a1be26b8af8eecab98783d08235bfca263793b61997244e785f5cf96e419a23f9b29137d820aab766ce986092180f1f5a690dc7767ef1df76e13315a5c8b04fb782")

# Données associées
associated_data = bytes.fromhex("80400c0600000000")

# Création du compteur
counter = int.from_bytes(nonce, byteorder='big')

# Création de l'objet de chiffrement
cipher = AES.new(key, AES.MODE_CTR, nonce=nonce, initial_value=counter)

# Décryptage
plaintext = cipher.decrypt(ciphertext)

# Conversion du résultat en hexadécimal
plaintext_hex = plaintext.hex()

print("Message décrypté :", plaintext_hex)