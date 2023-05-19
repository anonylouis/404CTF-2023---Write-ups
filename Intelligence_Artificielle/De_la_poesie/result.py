#!/usr/bin/python3
# coding: utf-8
# Code partiel, l'originial étant fait sur Jupyter
## Imports & Param's

import numpy as np
import pandas as pd
print("pandas")
import matplotlib
#matplotlib.use('agg')
import matplotlib.pyplot as plt
print("plt")
import random
import time
from keras.datasets import mnist

print("import finshed")

digit = mnist.load_data()
print("loaded !")

def displayImage(i):
	global digit
	plt.imshow(digit['images'][i], cmap='Greys_r')
	plt.show()

displayImage() 
# On met le type des images en float.
X0 = X0.astype('float32')
X1 = X1.astype('float32')
# On met les images sous la forme d'un vecteur.
X0 = X0.reshape(60000, 784)
X1 = X1.reshape(10000, 784) 
# On normalise les images.
X0 = X0 / 255.0
X1 = X1 / 255.0

print("normalized")
#Affichage de la 3ème image
n = 2
Y0_ = pd.get_dummies(Y0).values
Y1_ = pd.get_dummies(Y1).values
plt.imshow(X0[n, :].reshape(28, 28), cmap="gray")
plt.show()