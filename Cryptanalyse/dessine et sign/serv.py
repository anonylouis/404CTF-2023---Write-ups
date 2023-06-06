#!/bin/python3
from ECDSA import *
FLAG = "salut"

def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        d, x, y = extended_gcd(b, a % b)
        return d, y, x - (a // b) * y

def find_diophantine_solution(A, B, C, n):
    gcd, x0, y0 = extended_gcd(A, B)
    if C % gcd != 0:
        return None  # Pas de solution

    x = (C // gcd) * x0 % n
    y = (C // gcd) * y0 % n
    return x, y


p = 0xf1fd178c0b3ad58f10126de8ce42435b3961adbcabc8ca6de8fcf353d86e9c03
a = 0xf1fd178c0b3ad58f10126de8ce42435b3961adbcabc8ca6de8fcf353d86e9c00
b = 0xee353fca5428a9300d4aba754a44c00fdfec0c9ae4b1a1803075ed967b7bb73f
n = 0xf1fd178c0b3ad58f10126de8ce42435b53dc67e140d2bf941ffdd459c6d655e1
G = Point(0xb6b3d4c356c139eb31183d4749d423958c27d2dcaf98b70164c97a2dd98f5cff, 0x6142e0f7c8b204911f9271f0f3ecef8c2701c307e8e4c9e183115a1554062cfb)
E = Curve(a, b, p, n, G)
COUNTER_QUERY = 10

# print(E.PK)


m = ["a1", "a2"]
s = []
r = []
h = []

triche = []

for i in m :
    b = bytes.fromhex(i)
    sig = E.sign(b)
    r.append(sig[0])
    s.append(sig[1])
    h.append(bytes_to_long(sha256(b).digest()))
    nonce = bytes_to_long(E.compute_nonce(b))
    triche.append(nonce)

# eq 1
print((triche[0] * s[0] - r[0] * E.d1) % n)
print((h[0]) % n)


print("")
# eq 2
print((triche[1] * s[1] - r[1] * E.d1) % n)
print((h[1]) % n)

print("")

#NEW EQUATIONS :
print("")

A1 = (s[0] * r[1]) % n
B1 = (-1 * s[1] * r[0] ) % n
C1 = (h[0] * r[1] - h[1] * r[0]) % n

print((triche[0] * A1 + triche[1] * B1) % n)
print(C1 % n)

print("TEST TKTKT\n")


print((triche[0] * A1 + triche[1] * B1) % n)
print((C1) % n)

N = 16**12
A = (A1 + B1)

a = ((triche[0] - triche[1])) / N
k = (A * a - C1) // n


B = (-n)
C =  C1


print((A * a + B * k))
print(C1)


# particular_solution = find_diophantine_solution(A, B, C, N)

# print (particular_solution)
# gcd, x0, y0 = extended_gcd(A, B)
# a = A // gcd
# b = B // gcd

# print(((triche[0] % N) - particular_solution[0]) / B)