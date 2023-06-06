#!/bin/python3

from fastecdsa.curve import P521
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from hashlib import sha256
from solve_quadratic_congruence import solve_quadratic_congruence


q = P521.q

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

iv = f.readline()[:-1]
cipher = f.readline()

decrypt_d = m[0]

print("")

C1 = m[2] * pow(s[2], -1, q) * pow(r[1], -1, q) * s[1] - decrypt_d * pow(r[1], -1, q) * m[1] - m[1] * pow(s[1], -1, q) * s[0] * pow(r[0], -1, q)
C2 = pow(r[1], -1, q) * s[1] - s[0] * pow(r[0], -1, q)
C3 = m[1] * pow(r[1], -1, q) - m[0] * pow(r[0], -1, q)
C4 = r[1] * pow(s[1], -1, q) * s[0] * pow(r[0], -1, q) - r[2] * pow(s[2], -1, q) * pow(r[1], -1, q) * s[1] + decrypt_d
C1 %=q
C2 %=q
C3 %=q
C4 %=q

# # Equation 1
# print((C.sk * C4 + _B * C2 + _A * C3)  % q)
# print(C1  % q)


print("")

C5 = r[1] * pow(s[1], -1, q) * s[0] * pow(r[0], -1, q) -  s[2] * pow(r[2], -1, q) * pow(s[3], -1, q) * r[3] + 2 * decrypt_d
C6 = s[2] * pow(r[2], -1, q) - s[0] * pow(r[0], -1, q)
C7 = pow(r[2], -1, q) * m[2] - m[0] * pow(r[0], -1, q)
C8 = s[2] * pow(r[2], -1, q) * pow(s[3], -1, q) * m[3] - m[1] * pow(s[1], -1, q) * s[0] * pow(r[0], -1, q) - 2 * decrypt_d * pow(r[2], -1, q) * m[2]


C5 %=q
C6 %=q
C7 %=q
C8 %=q
#Equation 2

# print((C.sk * C5 + _B * C6 + _A * C7) % q)
# print(C8  % q)


print("")

C9  = m[1] * s[0]
C10 = -m[1] * r[0]
C11 = m[2]

C9 %=q
C10 %=q
C11 %=q

# eqatiom 3

# print((s[0] *  _K ) % q)
# print((m[0] + C.sk * r[0]) % q)

# print((C9 * _K + C10 * C.sk) % q)
# print(C11 % q)


#ON COMBINE EQ1 ET EQ2 :
print("")

# C4 * sk + C2 * B + C3 * A = C1
# C5 * SK + C6 * B + C7 * A = C8


# print((C.sk * C5 * pow(C7, -1, q) + _B  * C6 * pow(C7, -1, q) + _A ) % q)
# print((C8 * pow(C7, -1, q))  % q)

print("B en fonction de sk")

E2 = (C2 - C3 * C6 * pow(C7, -1, q)) 
E1 = (C4 - C3 * C5 * pow(C7, -1, q)) * pow(E2, -1, q)
E3 = (C1 - C3 * C8 * pow(C7, -1, q)) *  pow(E2, -1, q)
# print( _B  % q)
# print((E3 - E1 * C.sk)  % q)

print("\nA en fonction de sk")

F2 = (C3 - C2 * C7  * pow(C6, -1, q))
F3 = (C1 - C2 * C8 * pow(C6, -1, q)) * pow(F2, -1, q)
F1 = (C4 - C2 * C5 * pow(C6, -1, q)) * pow(F2, -1, q)
# print(_A  % q)
# print((F3 - C.sk * F1)  % q)

print("\nK en fonction de sk")

G1 = r[0] * pow(s[0], -1, q)
G2 = m[0] * pow(s[0], -1, q)
# print( _K % q)
# print((G2 + C.sk * G1) % q)


print("\n On insere tout dans eq2 :")

#print(((F3 - C.sk * F1) * (G2 + C.sk * G1) + _B) % q)

H1 = F3 * G1 - F1 * G2 - E1 - r[1] * pow(s[1], -1, q)
H2 = - (F1 * G1)
H3 = m[1] * pow(s[1], -1, q) - (F3 * G2 +  E3)

H1 *=  pow(H2, -1, q)
H3 *=  pow(H2, -1, q)

H3 *= -1
H1 %= q
H2 %= q
H3 %= q

# print((C.sk * C.sk + H1 * C.sk + H3) % q)

L = solve_quadratic_congruence(1, H1, H3, q)

for i in L :
    if i == L[0] :
        decrypt_iv = bytes.fromhex(iv)
        decrypt_key = sha256(str(i).encode()).digest()[:16]
        decrypt_aes = AES.new(decrypt_key , AES.MODE_CBC, iv=decrypt_iv)
        print(unpad(decrypt_aes.decrypt(bytes.fromhex(cipher)),16))

