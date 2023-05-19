#!/bin/python3
from functools import cmp_to_key
import sys

VOY="aeiouyAEIOUY"
alphabet="abcdefghijklmnopqrstuvwxyz"
FINAL = []


for n_arg in range(1, len(sys.argv)) :
	original= sys.argv[n_arg]
	text=original

	def regle1(s) :
		return s[::-1]

	def regle2(s) :
		if len(s) %2 == 0 :
			return s[len(s)//2:] + s[:len(s)//2]
		return s.replace(s[len(s)//2], "")

	def regle3(s) :
		if len(s) >= 3 :
			cpy = ""
			all_voyelle = ''.join([i for i in original if i in VOY])
			if s[2].isalpha() and s[2] not in VOY :
				c = 1
				for i in original :
					if i in VOY :
						cpy+=all_voyelle[c % len(all_voyelle)]
						c+=1
					else :
						cpy+=i
			else :
				c = -1
				for i in original :
					if i in VOY :
						cpy+=all_voyelle[c]
						c+=1
					else :
						cpy+=i
		else :
			return s
		return regle2(regle1(cpy))

	def vp(letter) :
		L=alphabet[:alphabet.find(letter.lower())][::-1]
		for j in L :
			if j in VOY :
				if letter == letter.lower() :
					return j
				else :
					return j.upper()

	def somm(n, mot) :
		st = 0
		for j in range(n-1, -1, -1) :
			if mot[j] in VOY :
				st+= ord(mot[j]) * (2**(n-j))
		return st


	global_cmp=""
	def key1(x) :
		return [global_cmp.count(x), 256-ord(x)]

	def regle4(s) :
		i = 0
		while i < len(s) :
			if s[i].isalpha() and s[i] not in VOY :
				to_insert = ord(vp(s[i])) + somm(i, s)
				to_insert = (to_insert % 95 ) + 32
				s = s[:i+1] + chr(to_insert) + s[i+1:]
			i+=1
		global global_cmp
		global_cmp=s
		L=sorted([i for i in global_cmp], key=key1, reverse=True)
		s = ''.join(L)
		return s


	# print(text)

	# text = regle1(text)
	# print(text)

	# text = regle2(text)
	# print(text)

	# text = regle3(text)
	# print(text)

	# text = regle4(text)
	# print(text)

	# print(regle4(regle3(regle2(regle1(original)))))
	FINAL.append(regle4(regle3(regle2(regle1(original)))))

print(" ".join(FINAL))