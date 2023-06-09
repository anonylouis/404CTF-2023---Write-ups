#!/bin/python3

import numpy as np

def print_matrix(M) :
	n = M.shape
	for i in range(n[0]) :
		for j in range(n[1]) :
			print("{:2d}".format(M[i][j]), end=" ")
		print("")

A = np.array([
	[ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
	[ 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
	[ 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 1],
	[ 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 3, 2, 1],
	[ 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 3, 2, 1],
	[ 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 5, 4, 3, 2, 1],
	[ 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 6, 5, 4, 3, 2, 1],
	[ 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 7, 6, 5, 4, 3, 2, 1],
	[ 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 8, 7, 6, 5, 4, 3, 2, 1],
	[10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
	[11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
	[12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,11,10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
	[13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,12,11,10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
	[14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,13,12,11,10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
	[15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,14,13,12,11,10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
	[16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,15,14,13,12,11,10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
	[17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,16,15,14,13,12,11,10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
	[18,18,18,18,18,18,18,18,18,18,18,18,18,18,17,16,15,14,13,12,11,10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
	[19,19,19,19,19,19,19,19,19,19,19,19,19,18,17,16,15,14,13,12,11,10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
	[20,20,20,20,20,20,20,20,20,20,20,20,19,18,17,16,15,14,13,12,11,10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
	[21,21,21,21,21,21,21,21,21,21,21,20,19,18,17,16,15,14,13,12,11,10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
	[22,22,22,22,22,22,22,22,22,22,21,20,19,18,17,16,15,14,13,12,11,10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
	[23,23,23,23,23,23,23,23,23,22,21,20,19,18,17,16,15,14,13,12,11,10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
	[24,24,24,24,24,24,24,24,23,22,21,20,19,18,17,16,15,14,13,12,11,10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
	[25,25,25,25,25,25,25,24,23,22,21,20,19,18,17,16,15,14,13,12,11,10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
	[ 0, 0, 0, 0, 0, 0,25,24,23,22,21,20,19,18,17,16,15,14,13,12,11,10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
	[ 1, 1, 1, 1, 1, 0,25,24,23,22,21,20,19,18,17,16,15,14,13,12,11,10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
	[ 2, 2, 2, 2, 1, 0,25,24,23,22,21,20,19,18,17,16,15,14,13,12,11,10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
	[ 3, 3, 3, 2, 1, 0,25,24,23,22,21,20,19,18,17,16,15,14,13,12,11,10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
	[ 4, 4, 3, 2, 1, 0,25,24,23,22,21,20,19,18,17,16,15,14,13,12,11,10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
	[ 5, 4, 3, 2, 1, 0,25,24,23,22,21,20,19,18,17,16,15,14,13,12,11,10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
	])

B = np.array([
	[ 9],[ 0],[13],[22],[20],[ 7],[12],[13],[ 3],[ 5],[15],[12],[ 5],[ 6],[ 3],[22],[ 2],[17],[12],[19],[17],[23],[25],[24],[19],[ 2],[17],[21],[23],[12],[23]
	])

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