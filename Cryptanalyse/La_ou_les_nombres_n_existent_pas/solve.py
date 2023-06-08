#!/bin/python3

from fastecdsa.curve import P521
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from hashlib import sha256
from solve_quadratic_congruence import solve_quadratic_congruence

def decrypt_flag(cipher, iv, sk):
    key = sha256(sk).digest()[:16]
    aes = AES.new(key , AES.MODE_CBC, iv=iv)
    flag = unpad(aes.decrypt(cipher), 16)
    print(flag)

# parsing
f = open("data.txt", "r")

m =[]
r =[]
s =[]

for i in range(4) :
    l = f.readline().split(" : ")
    m.append(int(l[0]))
    l = l[1][1:-2].split(",")
    r.append(int(l[0]))
    s.append(int(l[1]))

iv = bytes.fromhex(f.readline()[:-1])
cipher = bytes.fromhex(f.readline())

q = P521.q
d = m[0]

# Equation 3
C1 = (r[1] * pow(s[1], -1, q) * s[0] * pow(r[0], -1, q) - r[2] * pow(s[2], -1, q) * pow(r[1], -1, q) * s[1] + d) % q
C2 = (pow(r[1], -1, q) * s[1] - s[0] * pow(r[0], -1, q)) % q
C3 = (m[1] * pow(r[1], -1, q) - m[0] * pow(r[0], -1, q)) % q
C4 = (m[2] * pow(s[2], -1, q) * pow(r[1], -1, q) * s[1] - d * pow(r[1], -1, q) * m[1] - m[1] * pow(s[1], -1, q) * s[0] * pow(r[0], -1, q)) % q

# (C.sk * C1 + _B * C2 + _A * C3)  % q = C4 % q


#Equation 4
C5 = (r[1] * pow(s[1], -1, q) * s[0] * pow(r[0], -1, q) -  s[2] * pow(r[2], -1, q) * pow(s[3], -1, q) * r[3] + 2 * d ) % q
C6 = (s[2] * pow(r[2], -1, q) - s[0] * pow(r[0], -1, q) ) % q
C7 = (pow(r[2], -1, q) * m[2] - m[0] * pow(r[0], -1, q) ) % q
C8 = (s[2] * pow(r[2], -1, q) * pow(s[3], -1, q) * m[3] - m[1] * pow(s[1], -1, q) * s[0] * pow(r[0], -1, q) - 2 * d * pow(r[2], -1, q) * m[2] ) % q

# (C.sk * C5 + _B * C6 + _A * C7) % q = C8 % q

# a en fonction de sk 
tmp = (C3 - C2 * C7  * pow(C6, -1, q))
F1 = (C4 - C2 * C8 * pow(C6, -1, q)) * pow(tmp, -1, q)
F2 = (C1 - C2 * C5 * pow(C6, -1, q)) * pow(tmp, -1, q)
# a % q = (F1 - C.sk * F2)  % q)

# b en fonction de sk 
tmp = (C2 - C3 * C6 * pow(C7, -1, q))
E1 = (C4 - C3 * C8 * pow(C7, -1, q)) * pow(tmp, -1, q)
E2 = (C1 - C3 * C5 * pow(C7, -1, q)) * pow(tmp, -1, q)
# b % q = (E1 - E2 * C.sk)  % q)

# k en fonction de sk 
G1 = m[0] * pow(s[0], -1, q)
G2 = r[0] * pow(s[0], -1, q)
# k % q = (G1 + C.sk * G2) % q


# equation 2

H1 = (F2 * G2) % q
H2 = (F2 * G1 - F1 * G2 + E2 + r[1] * pow(s[1], -1, q)) % q
H3 = (m[1] * pow(s[1], -1, q) - F1 * G1 - E1) % q

# H1 * C.sk * C.sk + H2 * C.sk + H3) % q = 0

L = solve_quadratic_congruence(H1, H2, H3, q)

for i in L :
    try :
        sk = str(i).encode()
        decrypt_flag(cipher, iv, sk)
    except :
        continue
