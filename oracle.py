#!/bin/python3

from pwn import *
from Crypto.Util.number import long_to_bytes
import time

e = 65537

def get_oracle(_conn, _n) :
    _conn.sendline(str(_n))
    response = _conn.recvline_startswith((b'1',b'2',b'3',b'4',b'5',b'6',b'7',b'8',b'9')).decode()
    return int(response)

conn = remote('challenges.404ctf.fr',31674)

gift = int(conn.recvline_startswith((b'1',b'2',b'3',b'4',b'5',b'6',b'7',b'8',b'9')).decode())
n = int(conn.recvline_startswith("Initialisation").decode()[31:-29], 16)

L = [0, n-1]

while (L[1] - L[0]) > 1:
    mid = (L[0] + L[1]) // 2
    if (get_oracle(conn, pow(mid, e, n)) == mid) :
        L[0] = mid
    else :
        L[1] = mid

conn.close()


_q = L[1]
_p = n // _q
_d = pow(e, -1, (_p-1) * (_q-1))

print(long_to_bytes(pow(gift, _d, n)))

