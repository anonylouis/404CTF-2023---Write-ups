#!/bin/python3

import sys
from pwn import *
import numpy as np

alpha="abcdefghijklmnopqrstuvwxyz"
secret="pvfdhtuwgbpxfhocidqcznupamzsezp"

n = len(secret)
print("longueur =", n)

conn = remote('challenges.404ctf.fr',31682)
conn.sendlineafter("message en clair : ", 'a' * n)
data = conn.recvline()[19:19 + n].decode()
D = [alpha.find(l) for l in data]
M = []
for i in range(n) :
	str =  'a' * i + 'b' + 'a' * (n - i - 1)
	conn.sendlineafter("message en clair : ", str)
	data = conn.recvline()[19:19 +len(str)].decode()
	M.append([alpha.find(data[j]) - D[j] for j in range(n)])

conn.close()

A = np.zeros((n, n), dtype = int)
B = np.zeros((n, 1), dtype = int)

for i in range(n) :
	l = D[i]
	for j in range(n) :
		l += M[j][i] * alpha.find(secret[j])
		A[i][j] = M[j][i]

for i in range(n) :
	B[i] = alpha.find(secret[i]) - D[i]

A %= 26
B %= 26

AB = np.concatenate((A, B), axis=1)

for i in range(1, 31) :
	if i < 26 :
		AB[i] -= (i + 1) * AB[0]
	else :
		AB[i] -= (i - 25) * AB[0]
AB %= 26

AB[-1] *= 25
AB[-1] %= 26
AB[0]  -= AB[-1]
AB[1]  += AB[-1]
AB[-1] -= AB[1]

AB %= 26

for i in range(2,16) :
	AB[-i] *= 25
	AB[-i] %= 26
	AB[i-2]  -= 25 * AB[-i]
	AB[i-1]  -= 2 * AB[-i]
	AB[i] += AB[-i]
	AB[-i] -= AB[i]
	AB %= 26

for j in range(1, 15) :
	for i in range(j, 31-j) :
		AB[i] -= AB[i][-j-1] * AB[-j]
	AB %= 26

AB[15] -= AB[16]
AB[14] -= 25 * AB[16]
AB %= 26

X = AB[:, -1]

for i in range(len(X)) :
	print(alpha[int(X[i])], end="")
