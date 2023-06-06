#!/bin/python3

from pwn import *
import numpy as np

alpha="abcdefghijklmnopqrstuvwxy"
secret="ueomaspblbppadgidtfn"

conn = remote('challenges.404ctf.fr',31451)
A = np.zeros((5, 5), dtype = int)

for i in range(5) :
	conn.sendlineafter("message en clair : ", 'a'*i + 'b'+ 'a' * (4-i))
	data = conn.recvline()[19:24].decode()
	#print(data)
	for j in range(5) :
		A[j][i] = alpha.find(data[j])

conn.close()


M = np.concatenate((A, np.identity(5)), axis=1)

M[0] *= 14
M[0] %= 25
for i in range(5) :
	if i != 0 :
		M[i] -= M[i][0] * M[0]
M %= 25

M[1] *= 14
M[1] %= 25
for i in range(5) :
	if i != 1 :
		M[i] -= M[i][1] * M[1]
M %= 25

M[2] *= 13
M[2] %= 25
for i in range(5) :
	if i != 2 :
		M[i] -= M[i][2] * M[2]
M %= 25

M[3] -= M[4]
M[3] %= 25

M[3] *= 8
M[3] %= 25
for i in range(5) :
	if i != 3:
		M[i] -= M[i][3] * M[3]
M %= 25

M[4] *= 6
M[4] %= 25
for i in range(5) :
	if i != 4:
		M[i] -= M[i][4] * M[4]
M %= 25


invA = M[:, -5:]

#print(invA)

B = np.zeros((5, 1), dtype = int)


n = len(secret)
while n > 0:
	if n >= 5 :
		mot = secret[:5]
		secret=secret[5:]
		n-=5
	else :
		mot = secret + "a" * (5 - n)
		secret=""
		n = 0

	for i in range(5):
		B[i] = alpha.find(mot[i])

	X = np.dot(invA, B)
	X %= 25

	for i in range(5) :
		print(alpha[int(X[i])], end="")

