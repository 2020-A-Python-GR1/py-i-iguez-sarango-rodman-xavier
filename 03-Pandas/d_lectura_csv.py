# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 10:13:32 2020

@author: xavi2
"""
import pandas as pd
import os

path = "C://Users//xavi2//Documents//GitHub//py-iniguez-sarango-rodman-xavier//03-Pandas//data//artwork_data.csv"

df1 = pd.read_csv(
    path,
    nrows = 10)

columnas = ['id', 'artist', 'title', 'medium', 'year', 'acquisitionYear',
            'height', 'width', 'units']

df2 = pd.read_csv(
    path,
    nrows = 10,
    usecols = columnas)

df3 = pd.read_csv(
    path,
    nrows = 10,
    usecols = columnas,
    index_col = 'id') 

path_guardado = "C://Users//xavi2//Documents//GitHub//py-iniguez-sarango-rodman-xavier//03-Pandas//data//artwork_data.pickle"

df3.to_pickle(path_guardado)

df4 = pd.read_pickle(path_guardado)

















