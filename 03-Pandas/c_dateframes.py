# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 08:47:32 2020

@author: xavi2
"""

import numpy as np
import pandas as pd

arr_pand = np.random.randint(0,10,6).reshape(2,3)

df1 = pd.DataFrame(arr_pand)
s1 = df1[0]
s2 = df1[1]
s3 = df1[2]

df1[3] = s1
df1[4] = s1 * s2

datos_fisicos_uno = pd.DataFrame(
    arr_pand,
    columns = [
        'Estatura (cm)',
        'Peso (kg)',
        'Edad (anios)'])

datos_fisicos_dos = pd.DataFrame(
    arr_pand,
    columns = [
        'Estatura (cm)',
        'Peso (kg)',
        'Edad (anios)'],
    index = [
        'Rodman',
        'Xavier'])

serie_peso = datos_fisicos_dos['Peso (kg)']
datos_rodman = serie_peso['Rodman']
print(serie_peso)
print(datos_rodman)

df1.index = ['Rodman', 'Xavier']
df1.index = ['Wendy', 'Carolina']
df1.columns = ['A', 'B', 'C', 'D', 'E']















