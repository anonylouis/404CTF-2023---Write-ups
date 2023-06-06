#!/bin/python3
from PIL import Image
import numpy as np

def distance(a, b):
	return np.linalg.norm(np.array(a) - np.array(b))

def to_flou(c) :
	r,g,b = c
	modif_r,modif_g, modif_b = c
	while distance((r, g, b), (modif_r, modif_g, modif_b)) < 69 :
		if modif_r < 1 * max(modif_r, modif_g, modif_b) :
			modif_r +=1
		elif modif_g < 1* max(modif_r, modif_g, modif_b) :
			modif_g +=1
		#elif modif_b < 62 :
		#	modif_b +=1
		elif modif_b < max(modif_r, modif_g, modif_b) :
			modif_b +=1
		else :
			break
	while distance((r, g, b), (modif_r, modif_g, modif_b)) < 69 :
		if modif_g < 255 :
			modif_g +=1
		if modif_b < 255 :
			modif_b +=1
		if modif_r < 255 :
			modif_r += 1
		else :
			break
	if distance((r, g, b), (modif_r, modif_g, modif_b)) > 70 :
		modif_g -=1
	if distance((r, g, b), (modif_r, modif_g, modif_b)) > 70 :
		modif_b -=1
	if distance((r, g, b), (modif_r, modif_g, modif_b)) > 70 :
		modif_r -=1
	if distance((r, g, b), (modif_r, modif_g, modif_b)) > 70 :
		print("GROS CACA")
	return (modif_r, modif_g, modif_b)

def to_red(c) :
	r,g,b = c
	modif_r,modif_g, modif_b = c
	while distance((r, g, b), (modif_r, modif_g, modif_b)) < 69 :
		if modif_r < max(r,g,b) :
			modif_r +=1
		elif modif_g < max(r,g,b) :
			modif_g +=1
		elif modif_b < max(r,g,b) :
			modif_b +=1
		else :
			break
	
	if max(r,g,b) < -100 :
		while distance((r, g, b), (modif_r, modif_g, modif_b)) < 69 :
			if modif_r < 0 :
				modif_r +=1
			if modif_g < 0 :
				modif_g +=1
			if modif_b < 0 :
				modif_b +=1
			else :
				break
	else :
		while distance((r, g, b), (modif_r, modif_g, modif_b)) < 69 :
			if modif_r > 0 :
				modif_r -=1
			if modif_g > 0 :
				modif_g -=1
			if modif_b > 0 :
				modif_b -=1
			else :
				break
	if distance((r, g, b), (modif_r, modif_g, modif_b)) > 70 :
		modif_g+=1
	if distance((r, g, b), (modif_r, modif_g, modif_b)) > 70 :
		modif_b+=1
	if distance((r, g, b), (modif_r, modif_g, modif_b)) > 70 :
		print("GROS CACA 3")
		modif_b+=1
	return (modif_r, modif_g, modif_b)

SIZE=224

chat = Image.open("chat.jpg")
teepot = Image.open("teepot3.jpg")
# for i in range(0, SIZE) :
# 	for j in range(0, 15) :
# 		teepot.putpixel((j, i), chat.getpixel((j,i)))

# for i in range(0, 17) :
# 	for j in range(0, SIZE) :
# 		teepot.putpixel((j, i), chat.getpixel((j,i)))

# for i in range(223, 199, -1) :
# 	for j in range(0, SIZE) :
# 		teepot.putpixel((j, i), chat.getpixel((j,i)))
	
# for i in range(0, SIZE) :
# 	for j in range(223, 208, -1) :
# 		teepot.putpixel((j, i), chat.getpixel((j,i)))

for i in range(SIZE) :
	for j in range(SIZE) :
		
		if distance(teepot.getpixel((i, j)), (186, 242, 242)) < 30:
			#print("ici c blanco", i, j)
			#to_flou(chat.getpixel((i, j)))
			#teepot.putpixel((i, j), to_flou(chat.getpixel((i, j))))
			teepot.putpixel((i, j), (255, 255, 255))
		else :
		  	teepot.putpixel((i, j), to_red(chat.getpixel((i, j))))




teepot.save('modif.jpg')