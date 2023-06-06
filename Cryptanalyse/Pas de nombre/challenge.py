#!/bin/python3

from fastecdsa.curve import P521
from random import randint
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from hashlib import sha256
from os import urandom
import numpy as np


# flag = b'VOICI UN MESSAGE SECRET'

# class Curve:

#     def __init__(self, a, b, d, sk, seed):
#         self.C = P521
#         self.G = P521.G
#         self.q = P521.q
#         self.a = a
#         self.b = b
#         self.d = d
#         self.sk = sk
#         self.k = seed
#         self.pk = sk * self.G

#     def get_next_a(self):
#         self.a = (self.a + self.d) % self.q

#     def get_next_nonce(self):
#         self.get_next_a()
#         self.k = (self.a * self.k + self.b) % self.q

#     def sign(self, m):
#         self.get_next_nonce()
#         #assert self.q > m > 0
        
#         # if (m == self.d) :
#         #     print("k =       ", self.k)
#         P = self.k * self.G
#         r = P.x

#         #assert r > 0
        

#         s = (pow(self.k, -1, self.q) * (m + self.sk * r)) % self.q
        
#         # if (m == self.d) :
#         #     print((s * self.k) %q)
#         #Si on a  self.k, on a self.sk !! 

#         # if (m == self.d) :
#         #     print("k =", self.k)
#             # first_part= (pow(self.k, -1, self.q) * m)
#             # second_part= (pow(self.k, -1, self.q) * r * self.sk) % self.q

#             # print("B         =", (first_part * pow(r, -1, self.q) + self.sk * pow(self.k, -1, self.q) ) % self.q )
#             # print("B perso   =",  (s * pow(r, -1, self.q)) % self.q)
#         # if (m == self.d) :
#         #     print("sk = ", self.sk)
#         #     A = ((s * self.k - m) * pow(r, -1, self.q)) % self.q
#         #     print("A  = ", A)

#         #assert s > 0
#         return r, s

#     def encrypt_flag(self, flag):
#         iv = urandom(16)
#         key = sha256(str(self.sk).encode()).digest()[:16]
#         #print(("key =", key))
#         aes = AES.new(key, AES.MODE_CBC, iv=iv)
#         ciphertext = aes.encrypt(pad(flag, 16))
#         return ciphertext.hex(), iv.hex()


q = P521.q

# #   Curve(      a,              b,             d,           sk,             k      )
# C = Curve(randint(0, q), randint(0, q), randint(0, q), randint(0, q), randint(0, q))
# # f = open("data.txt", "w")


# _K = ((C.a + C.d) *C.k + C.b ) % q
# _A = (C.a + 2*C.d) % q
# _B = C.b

# m = [pow(C.d, i, q) for i in range(1, 5)]

# signatures = [C.sign(m) for m in m]

# # for i in range(4):
# #     f.write(f"{m[i]} : {signatures[i]}\n")
# cipher, iv = C.encrypt_flag(flag)
# # f.write(iv+"\n")
# # f.write(cipher)

f = open("original.txt", "r")


m =[]
r =[]
s =[]

for i in range(4) :
    l = f.readline().split(" : ")
    m.append(int(l[0]))
    print(l[1])
    l = l[1][1:-2].split(",")
    r.append(int(l[0]))
    s.append(int(l[1]))

print(m)
print(r)
print(s)

iv = f.readline()[:-1]

print(iv)

cipher = f.readline()

print(cipher)


decrypt_d = m[0]

#OBJECTIF : AVOIR C.sk !!

# decrypt_iv = bytes.fromhex(iv)
# decrypt_key = sha256(str(C.sk).encode()).digest()[:16]

# # print('iv =', decrypt_iv)
# # print("key =", decrypt_key)

# decrypt_aes = AES.new(decrypt_key , AES.MODE_CBC, iv=decrypt_iv)
#print(unpad(decrypt_aes.decrypt(bytes.fromhex(cipher)),16))

# s = [i[1] for i in signatures]
# r = [i[0] for i in signatures]


# inconnues : _A, _B, C.sk, _K



# eq 1

# print((s[0] *  _K ) % q)
# print((m[0] + C.sk * r[0]) % q)

# # eq 2

# print((s[1] * (_A * _K + _B) ) % q)
# print((m[1] + C.sk * r[1]) % q)

# # eq 3

# print((s[2] * ((_A + decrypt_d) * (_A * _K + _B) + _B)) % q)
# print((m[2] + C.sk * r[2]) % q)

# # eq 4

# print((s[3] * ((_A + 2*decrypt_d)*((_A + decrypt_d) * (_A * _K + _B) + _B) + _B)) % q)
# print((m[3] + C.sk * r[3]) % q)


# eq 5

# print((s[0] *  _A * k ) % q)
# print((m[0] + C.sk * r[0]) % q)

## ECHEC

# 1ere etape : isoler K dans la premiere equation :

# print(_K % q)
# print((m[0] * pow(s[0], -1, q) + C.sk * r[0] * pow(s[0], -1, q))% q)
# # K en fonction de  sk

# print("")
# # 2eme etape : inserer K dans l equation 2 !

# print(_B % q)
# print((C.sk * r[1] * pow(s[1], -1, q) - _A * s[1] * C.sk * r[0] * pow(s[0], -1, q) * pow(s[1], -1, q) + m[1] * pow(s[1], -1, q) - _A * m[0] * pow(s[0], -1, q)) % q)
# # B en fonction de A et sk

# print("")
# # 3eme etape :
# print((s[2] * ((_A + decrypt_d) * (_A * _K + _B) + _B)) % q)
# print((m[2] + C.sk * r[2]) % q)


## DEUXIEME TENTATIVE :

# print((_A * (m[2] + C.sk * r[2]) * pow(s[2], -1, q) + 2 * decrypt_d * (m[2] + C.sk * r[2]) * pow(s[2], -1, q) + _B) % q)


# print((m[3] * pow(s[3], -1, q) + C.sk * r[3] * pow(s[3], -1, q)) % q)


# print((_A * C.sk)  % q)
# print((m[1] * pow(s[1], -1, q) * s[0] * pow(r[0], -1, q) + C.sk * r[1] * pow(s[1], -1, q) * s[0] * pow(r[0], -1, q) - _B * s[0] * pow(r[0], -1, q) - _A * m[0] * pow(s[0], -1, q) * s[0] * pow(r[0], -1, q)) % q)
# tranforme A*sk en fonction de sk, de _A et de _B


# TROISIEME TENTATIVE :

# _A   _B   C.sk    _K
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

def pow_mod(base, exponent, modulus):
    """
    Computing Modular exponentiation: base ^ exponent (mod modulus)

    Parameters
    ----------
    base : integer
    exponent : integer
    modulus : unsigned integer

    Returns
    -------
    int
        Result of calculation

    """
    return pow(base, exponent, modulus)


def inverse(a, p):
    """
    Computing multiplicative inverses in modular structures

    Parameters
    ----------
    a : integer
    p : unsigned integer

    Returns
    -------
    int
        Inverse of a (mod p)

    """
    t, newt = 0, 1
    r, newr = p, a

    while newr != 0:
        quotient = r // newr
        t, newt = newt, t - quotient * newt
        r, newr = newr, r - quotient * newr

    if r > 1:
        return None  # Vi p nguyen to nen truong hop nay khong xay ra

    if t < 0:
        t = t + p

    return t


def legendre(a, p):
    """
    Legendre function (a/p): (a/p) = a^((p-1)/2) (mod p)

    Parameters
    ----------
    a : integer
    p : unsigned integer

    Returns
    -------
    int
        Result of Legendre function

    """
    return pow_mod(a, (p - 1) // 2, p)


def tonelli_shanks(alpha, p):
    """
    Solve a congruence equation with Tonelli-Shanks algorithm:
        x^2 = alpha (mod p)
    With alpha \in Z_p, p is a prime number

    Parameters
    ----------
    alpha : integer
    p : unsigned integer

    Returns
    -------
    int
        One beta solution, the other can calculate by p - beta
    None
        No solution

    """
    if legendre(alpha, p) != 1:
        return None  # Vo nghiem

    q = p - 1
    s = 0

    while q % 2 == 0:
        q //= 2
        s += 1

    if s == 1:
        return pow_mod(alpha, (p + 1) // 4, p)

    for z in range(2, p):
        if p - 1 == legendre(z, p):
            break

    c = pow_mod(z, q, p)
    r = pow_mod(alpha, (q + 1) // 2, p)
    t = pow_mod(alpha, q, p)
    m = s
    t2 = 0

    while (t - 1) % p != 0:
        t2 = (t * t) % p

        for i in range(1, m):
            if (t2 - 1) % p == 0:
                break

            t2 = (t2 * t2) % p

        b = pow_mod(c, 1 << (m - i - 1), p)
        r = (r * b) % p
        c = (b * b) % p
        t = (t * c) % p
        m = i
    return r


def solve_congruence(a, b, p):
    """
    Solve a congruence equation:
        a*x = b (mod p)
    With a, b \in Z_p, p is a prime number

    Parameters
    ----------
    a : integer
    b : integer
    p : unsigned integer

    Returns
    -------
    int
        Single unique solution
    []
        Infinitely many solutions
    None
        No solution

    """
    if a == 0:
        if b == 0:
            return []  # Vo so nghiem
        else:
            return None  # Vo nghiem
    else:
        return b * inverse(a, p) % p


def solve_quadratic_congruence(a, b, c, p):
    """
    Solve a quadratic congruence equation:
        a*x^2 + b*x + c = 0 (mod p)
    With a, b, c \in Z_p, p is a prime number less than 4 billion
    ...

    Parameters
    ----------
    a : integer
    b : integer
    c : integer
    p : unsigned integer

    Returns
    -------
    [int, int]
        Two solution of equation
    []
        Infinitely many solutions
    None
        No solution

    """
    if a == 0:
        return solve_congruence(b, -c, p)
    else:
        a_inv = inverse(a, p)
        ba = (b * a_inv) % p
        ca = (c * a_inv) % p
        b_div_2 = (ba * inverse(2, p)) % p
        alpha = (pow_mod(b_div_2, 2, p) - ca) % p
        y = tonelli_shanks(alpha, p)

        if y is None:
            return None  # Vo nghiem

        x1 = (y - b_div_2) % p
        x2 = (p - y - b_div_2) % p

        return [x1, x2]

# print("On veut C.sk =", C.sk)
L = solve_quadratic_congruence(1, H1, H3, q)

for i in L :
    if i == L[0] :
        decrypt_iv = bytes.fromhex(iv)
        decrypt_key = sha256(str(i).encode()).digest()[:16]

        # print('iv =', decrypt_iv)
        # print("key =", decrypt_key)

        decrypt_aes = AES.new(decrypt_key , AES.MODE_CBC, iv=decrypt_iv)
        print(unpad(decrypt_aes.decrypt(bytes.fromhex(cipher)),16))


#equation 4 
# print("")

# C12 = s[2] * pow(r[2], -1, q) * pow(s[3], -1, q) * m[3] - m[1] * pow(s[1], -1, q) * s[0] * pow(r[0], -1, q)
# C13 = 2 * decrypt_d * pow(r[2], -1, q) * s[0] * m[1]
# C14 = C5  -  2 * decrypt_d * pow(r[2], -1, q) * m[1] * r[0]

# C12%=q
# C13%=q
# C14%=q

# print((C13 * _K + C.sk * C14 + _B * C6 + _A * C7) % q)
# print((C12)% q)

# print("")


# A00, A01, A02, A03, B00, B01, B02, B03 = C13 , C14 , C6 , C7 , 1, 0 , 0, 0
# A10, A11, A12, A13, B10, B11, B12, B13 = 0   , C5  , C6 , C7 , 0, 1 , 0, 0
# A20, A21, A22, A23, B20, B21, B22, B23 = C9  , C10 , 0  , 0  , 0, 0 , 1, 0
# A30, A31, A32, A33, B30, B31, B32, B33 = 0   , C4  , C2  , C3, 0, 0 , 0, 1

# L0 = [A00, A01, A02, A03, B00, B01, B02, B03]
# L1 = [A10, A11, A12, A13, B10, B11, B12, B13]
# L2 = [A20, A21, A22, A23, B20, B21, B22, B23]
# L3 = [A30, A31, A32, A33, B30, B31, B32, B33]


# L0 = [(i * pow(C13, -1, q) ) % q for i in L0]
# L2 = [(L2[i] - L2[i] * L0[i]) % q for i in range(len(L3))]


# tmp = L1[1]
# L1 = [(i * pow(tmp, -1, q) ) % q for i in L1]

# L0 = [(L0[i] - L0[i] * L1[i]) % q for i in range(len(L3))]
# L2 = [(L2[i] - L2[i] * L1[i]) % q for i in range(len(L3))]
# L3 = [(L3[i] - L3[i] * L1[i]) % q for i in range(len(L3))]


# tmp = L3[3]
# L3 = [(i * pow(tmp, -1, q) ) % q for i in L3]

# L0 = [(L0[i] - L0[i] * L3[i]) % q for i in range(len(L3))]
# L1 = [(L1[i] - L1[i] * L3[i]) % q for i in range(len(L3))]
# L2 = [(L2[i] - L2[i] * L3[i]) % q for i in range(len(L3))]

# print(L0)
# print(L1)
# print(L2)
# print(L3)