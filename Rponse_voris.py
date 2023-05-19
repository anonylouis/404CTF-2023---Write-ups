#!/bin/python3

import sys
# from pwn import *

def f(str) :
	conn = remote('challenges.404ctf.fr',30944)

	conn.sendlineafter("message en clair : ", str)
	data = conn.recvline()
	print(data +"!!!!!!!!!!!!!!!!!")
	conn.close()


# alpha="abcdefghijklmnopqrstuvwxyz"

# secret="pvfdhtuwgbpxfhocidqcznupamzsezp"

# mot = sys.argv[1]
# r = ""
# if (len(mot) == 1) :
# 	r += alpha[(alpha.find(mot[0]) + 2) % 26]

# if (len(mot) == 2) :
# 	r += alpha[(16 + 1 * alpha.find(mot[0]) + 1 * alpha.find(mot[1])) % 26]
# 	r += alpha[(5  + 2 * alpha.find(mot[0]) + 1 * alpha.find(mot[1])) % 26]

# if (len(mot) == 3) :
# 	r += alpha[(3  + 1 * alpha.find(mot[0]) + 1 * alpha.find(mot[1]) + 1 * alpha.find(mot[2])) % 26]
# 	r += alpha[(6  + 2 * alpha.find(mot[0]) + 2 * alpha.find(mot[1]) + 1 * alpha.find(mot[2])) % 26]
# 	r += alpha[(20 + 3 * alpha.find(mot[0]) + 2 * alpha.find(mot[1]) + 1 * alpha.find(mot[2])) % 26]



# if (len(mot) == len(secret)) :
# 	r += ""

# print(r)

print(f("aa"))