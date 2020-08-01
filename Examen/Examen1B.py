# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 09:07:38 2020

@author: xavi2
"""
import numpy as np

"2"
vector_ceros = np.zeros(10)
print(vector_ceros)

"3"
vector_ceros_5 = np.zeros(10)
vector_ceros_5[5] = 1
print(vector_ceros)

"4"
vector_50 = np.arange(50)
print(vector_50)
vector_50[::-1]

"5"
matriz_3x3 = np.random.randint(0,8,(3,3))
print(matriz_3x3)

"6"
arreglo = [1,2,0,0,4,0]


"7"
matriz_idetidad = np.eye(3)