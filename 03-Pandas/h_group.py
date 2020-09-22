# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 09:55:54 2020

@author: xavi2
"""

import pandas as pd
import math
import numpy as np

path = "C://Users//xavi2//Documents//GitHub//py-iniguez-sarango-rodman-xavier//03-Pandas//data//artwork_data.pickle"

df = pd.read_pickle(path)

seccion_df = df.iloc[49980:500019,:].copy()

df_agrupar_artista = seccion_df.groupby('artist')

print(type(df_agrupar_artista))

for columna, df_agrupado in df_agrupar_artista:
    print(type(columna))
    print(columna)
    print(type(df_agrupado))
    print(df_agrupado)

a     
    
