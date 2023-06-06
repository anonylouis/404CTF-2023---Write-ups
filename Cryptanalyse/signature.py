#!/bin/python3

from hashlib import md5 as hash
from dataclasses import dataclass
import json, os

# in bits
BLOCK_SIZE = 4
CHECKSUM_SIZE = 2*BLOCK_SIZE
MESSAGE_SIZE = 64*BLOCK_SIZE

FLAG = "coucou"


def pad_msg(data: bytes, size: int):
    return data + b'\x00' * (size - len(data))

def convol_hash(data: bytes, power: int):
    acc = data
    for _ in range(power):
        acc = hash(acc).digest()
    return acc

def checksum(data: bytes, block_size: int, checksum_size: int, message_size: int):
    bindata = f'{int.from_bytes(data, "big"):0b}'.zfill(message_size)
    acc = 0
    for i in range(0, message_size, block_size):
        acc += 2**block_size - int(bindata[i:i+block_size], 2) - 1
    acc %= 2**checksum_size
    return acc.to_bytes(checksum_size // 8, 'big')

@dataclass
class WinternitzPrivKey:
    secrets: list[bytes]
    block_size: int = BLOCK_SIZE
    checksum_size: int = CHECKSUM_SIZE

    def public_key(self):
        return WinternitzPubKey([convol_hash(s, 2**self.block_size) for s in self.secrets], self.block_size, self.checksum_size)

    def sign(self, data: bytes):
        signature_size = len(self.secrets)*self.block_size
        data_size = signature_size - self.checksum_size
        assert len(data) * 8 < data_size, "The message you want to sign is too long"
        padded_data = pad_msg(data, data_size // 8)
        cksum = checksum(padded_data, self.block_size, self.checksum_size, data_size)
        plaintext = padded_data + cksum
        binpt = f'{int.from_bytes(plaintext, "big"):0b}'.zfill(signature_size)
        
        print("private bindata = ", binpt)
        sig = []
        for i in range(0, signature_size, self.block_size):
            x = convol_hash(self.secrets[i//self.block_size], int(binpt[i:i+self.block_size], 2))
            if i==0:
                print("first = ", int(binpt[i:i+self.block_size], 2))
            sig.append(x)
        return sig

@dataclass
class WinternitzPubKey:
    public: list[bytes]
    block_size: int = BLOCK_SIZE
    checksum_size: int = CHECKSUM_SIZE

    def verify(self, data: bytes, sig: list[bytes]):
        signature_size = len(self.public) * self.block_size 
        
        print("public = ", len(self.public))

        data_size = signature_size - self.checksum_size
        
        print("data size :", data_size)
        
        assert len(sig) == len(self.public), "Signature size does not match key size"

        print("len data = ", len(data))
        assert len(data) * 8 <= data_size, "The message you want to verify is too long"  #32 chars max !!
        
        padded_data = pad_msg(data, data_size // 8) #on pad pour avoir 32 char !
        
        print("pad message : ", padded_data)
        cksum = checksum(padded_data, self.block_size, self.checksum_size, data_size)
        
        plaintext = padded_data + cksum
        print("plaintext = ", plaintext)
        bindata = f'{int.from_bytes(plaintext, "big"):0b}'.zfill(signature_size)
        print("bindata = ", bindata)
        for i in range(0, len(bindata), self.block_size): #on regarde par bloc de 4 !
            exp = 2**self.block_size - int(bindata[i:i+self.block_size], 2)
            # exp = 16 - int du bloc de 4 !
            if i == 0:
                print("e = ", exp)
                print("le bloc publique = ", self.public[i//self.block_size])
                print("donc si jamais 10 = ", convol_hash(sig[i//self.block_size], 10))
                
            if convol_hash(sig[i//self.block_size], exp) != self.public[i//self.block_size]:
                print(i//self.block_size, "exp =", exp, sig[i//self.block_size], self.public[i//self.block_size])
                return False
            else :
                print("OK", i//self.block_size)
        return True




def challenge(str):
    privkey = WinternitzPrivKey([hash(os.urandom(32)).digest() for i in range((MESSAGE_SIZE + CHECKSUM_SIZE) // BLOCK_SIZE)])
    pubkey = privkey.public_key()
    msg = b"SALUT CA VA?"
    sig = [x.hex() for x in privkey.sign(msg)]
    
    initial = json.dumps({"msg": msg.hex(), "sig": sig})
    initial += '\n'
    print(initial)
    print("premier bloc convol hash * 11 = ", convol_hash(bytes.fromhex(sig[0]), 11))

	# A FAIRE !!!!!!!!!!
    tmp="010100110100000101001100010101010101010000100000010000110100000100100000010101100100000100111111000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001011110"
    obj="011001110110100101101101011011010110010100100000011001100110110001100001011001110111101001011111011000010110000101100001011000010110000101100001011000010110000101100001011000010110000101100001011000010000000000000000000000000000000000000000000000000000000010111111"

    for l in range(0, 256+8, 4):
        if (int(obj[l:l+4], 2) - int(tmp[l:l+4], 2)) >= 0 :
            sig[l//4] = convol_hash(bytes.fromhex(sig[l//4]), int(obj[l:l+4], 2) - int(tmp[l:l+4], 2)).hex()
        else :
            print(l//4)
            print ("obj = ", int(obj[l:l+4], 2))
            print ("tmp = ", int(tmp[l:l+4], 2))
            #sig[l//4] = convol_hash(bytes.fromhex(sig[l//4]), int(tmp[l:l+4], 2) - int(obj[l:l+4], 2)).hex()

    str = json.dumps({"msg": b'gimme flagz_aaaaaaaaaaaaa'.hex(), "sig": sig})

    try:
        user_input = str
        request = json.loads(user_input)
        data = bytes.fromhex(request["msg"])
        sig = [bytes.fromhex(x) for x in request["sig"]]
        if data.startswith(b'gimme flagz'):
            valid = pubkey.verify(data, sig)
            if valid:
                response = json.dumps({"flag": FLAG})
            else:
                response = json.dumps({"error": "The signature is not valid"})
        else:
            response = json.dumps({"error": "Your message is not interesting, sorry"})
        response += '\n'
        print(response)
    except Exception as e:
        response = json.dumps({"error": "An unexpected error occurred"})
        response += '\n'
        print(response)
    finally:
        exit()

# if __name__ == "__main__":
#     challenge()

str="{\"msg\": \"67696D6D6520666C61677A\", \"sig\": [\"b7edfc3dc965c80d7b5219e82dcbab14\", \"3ccbdf8cd4eff3800e07ce0f282d36c1\", \"5215fe23b4c99163c1dd4fc777f53b96\", \"9f37623db70c1e013d993b0f1ed2b9ec\", \"aff3e73db550ad9a9e78b52b5b4d464a\", \"15bdeb30f480fbee330a3a834e095c3a\", \"bd2565589e9bac37e0e0bf386c4c762d\", \"855465c0cc8fe6bf04002509bf86c94f\", \"467639924d7d99cef04d5a1a18cdfea7\", \"68071b447a3670810a4b23c208a1a469\", \"eddd9db5d9af4ca3aa2de7e19305fcb1\", \"082cd31ad30822b70733d164807e2087\", \"0851964954bd45b507ee7feae2ddd870\", \"29fc68d9be1343ae16065ac9387409e3\", \"5af59cca3a017e74cc20bf8de296f93c\", \"4811e4052b54cec2ebdc6a9b3be6e44f\", \"e77c471f80bf9b572d3456382dc90775\", \"0388cb8ba2786975580ab9f46e62dd5d\", \"c2f343f6f3c853c1ae247f2c0f8419d1\", \"c60d751399651f8823da527f2346f417\", \"e045355c3b9a9061d78d5c768b6264bc\", \"00065c5ebb13087e2d5413845bda8254\", \"bfcccd2220eb2eea18ce40e022b7598d\", \"fde98f9f3417b6a3402b3119f7935c7a\", \"fea695380af2cabe50eac93742d747d5\", \"feb5380336b035234a71529b73bdeee1\", \"dd32d35d663f13f4550777eac5b15d21\", \"0a8433b0cd6bda852fefae337d9783d4\", \"f8c7d6477f84cddf25434e5d471b2cc1\", \"861dac0c3d486d53b194648090effb1c\", \"97e51c7e98ff83ef86232bcae95dcb7b\", \"a4a70671e713bddc07a9c0bf5a6666b3\", \"fb202200fa7b1dcc4524ed946fd2ccd4\", \"047a4c7b1ba9607ede6bab0b930b0a4f\", \"9a70a22f34f219ca4f18c1fdb0bdf8a1\", \"4416a3e3330588f54d0a2b999cb0b24a\", \"bba6a76ff163578662074bbff0049edb\", \"7978ebbed8c45f59586c627b0660a8a3\", \"7dbb1ad103043cda37444aa924efebf3\", \"1ffc986fade4505ba95637d6f0a5788e\", \"4f6ff7ebcc38c34dabb0fec0314af7bf\", \"171454421725e06b1bf3b25c94d88af0\", \"1bf3723b8a43e09ef09e34042b9a3283\", \"7b1b104522eed4a5dc00b07e69491026\", \"c7b8360acf3785dbf025915d08b52f5b\", \"37bce76bc141240298b0d85ea7ac15f1\", \"ff71e643c4fa3912ffce43ebca77f6c5\", \"6ba3652195394202c40aad54d2117792\", \"bb0ec63a851517d26afa0a34ddeaff73\", \"1948953a3f81bfdabb49de87ca8893d2\", \"56398a31ee8abf1ab5cfedec07c1fc96\", \"878a6a6755ff49f608da7c897987225f\", \"3d489f0a03d18f0276cb83089e0b6422\", \"797fe5ec67b39477e399113a835c91f6\", \"5d0e9547b7dc3308c0b8e6bd2856c487\", \"4c09a96572e5bb49bc914b54c77a4beb\", \"e4f3c82c3737d2ce684f5e346acee64a\", \"36b6acd513944b18b23dad9dc9fa658b\", \"93d8a0a87fb39a273733249d2d844e1a\", \"47bbd280dc1105f5a0d861d849bdf1d5\", \"0d10d963abffe4972510264cc55d2078\", \"b6cebfa6a42f4fadcef742401d7d3c60\", \"df85b51a6bba573f7f34787d186bae96\", \"2e77c00ab655c9dfbf0bb1b202089eb0\", \"63d9293dca3ab340220bd71434f0c112\", \"011456a391a4a553ad535eb80e72cd22\"]}"
request=json.loads(str)
data = bytes.fromhex(request["msg"])

challenge(str)


