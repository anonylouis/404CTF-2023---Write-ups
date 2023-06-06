#!/bin/python3

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