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

indice = []
for i in range(len(arreglo)):
    if arreglo[i] is not 0:
        indice.append(i)
print(indice)

"7"
matriz_idetidad = np.eye(3)
print(matriz_idetidad)

"8"
matriz3_3_3 = np.random.random((3,3,3))
print(matriz3_3_3)

"9"
matriz = np.arange(100).reshape(10,10)
matriz.min()
matriz.max()

"10"


"11"
import pandas as pd

mylist = list('abcedfghijklmnopqrstuvwxyz')
myarr = np.arange(26)
mydict = dict(zip(mylist, myarr))

serie_1 = pd.Series(mylist)
serie_2 = pd.Series(myarr)
serie_3 = pd.Series(mydict)

"12"
ser = pd.Series(mydict)

df1 = pd.DataFrame(ser)
columnas = pd.DataFrame(
    ser,
    columns = [
        'mydic'])

"13"
ser1 = pd.Series(list('abcedfghijklmnopqrstuvwxyz'))
ser2 = pd.Series(np.arange(26))

lista_serie = (ser1, ser2)
df2 = pd.DataFrame(lista_serie)

"14"
ser1 = pd.Series([1, 2, 3, 4, 5])
ser2 = pd.Series([4, 5, 6, 7, 8])

"15"
ser1 = pd.Series([1, 2, 3, 4, 5])
ser2 = pd.Series([4, 5, 6, 7, 8])

"16"
ser = pd.Series(np.take(list('abcdefgh'), np.random.randint(8, size=30)))

df3 = pd.DataFrame(ser)
df3.value_counts()



















