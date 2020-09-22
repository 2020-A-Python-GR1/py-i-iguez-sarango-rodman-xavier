# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 07:48:43 2020

@author: xavi2
"""
import numpy as np
import pandas as pd
import datetime
datetime.datetime.strptime


# 1.
arr_pand = np.random.randint(0,10,60).reshape(10,6)
df1 = pd.DataFrame(arr_pand)
registros = df1.iloc[0:5,0:5]

# 2.
arr_pand2 = np.random.randint((6,4))
index = pd.date_range('2020-09-21', periods=6)
df2 = pd.DataFrame(arr_pand, index=index, columns=list('ABCD')) 

# 4. 
arr_pand3 = np.random.randint(0,10,60).reshape(10,6)

df3 = pd.DataFrame(arr_pand3)
df3.columns = ['A', 'B', 'C', 'D', 'E','F']

columna1 = df3.iloc[0]
valores = df3.iloc[0:1] 
print(columna1)
print(valores)

# 5.

arr_pand4 = np.random.randint(0,10,60).reshape(10,6)

df4 = pd.DataFrame(arr_pand4)
df4.columns = ['A', 'B', 'C', 'D', 'E','F']

# 6.
arr_pand4 = np.random.randint(0,10,60).reshape(10,6)
df5 = pd.DataFrame(arr_pand4)
df5.columns = ['A', 'B', 'C', 'D', 'E','F']
df5.transpose()

# 8.
arr_pand4 = np.random.randint(0,10,60).reshape(10,6)
df6 = pd.DataFrame(arr_pand4)
df6.columns = ['A', 'B', 'C', 'D', 'E','F']
df6[df6 > 7]

# 9.
arr_pand4 = np.random.randint(0,10,60).reshape(10,6)
df7 = pd.DataFrame(arr_pand4)
df7 = df7.where(df7<7)
df7 = df7.fillna(0)

# 10.
arr_pand4 = np.random.randint(0,10,60).reshape(10,6)
df8 = pd.DataFrame(arr_pand4)
media = df8.mean()
media
mediana = df8.median()
mediana
promedio = np.average(df8)
promedio

# 11.
arr_pand4 = np.random.randint(0,10,60).reshape(10,6)
df9 = pd.DataFrame(arr_pand4)

arr_pand4 = np.random.randint(0,10,60).reshape(10,6)
df10 = pd.DataFrame(arr_pand4)

df9.append(df10)

# 12.
arr_pand4 = np.random.randint(0,10,60).reshape(10,6)
df11 = pd.DataFrame(arr_pand4)

# 13.
arr_pand4 = np.random.randint(0,10,60).reshape(10,6)
df12 = pd.DataFrame(arr_pand4)
df6.columns = ['A', 'B', 'C', 'D', 'E','F']
df12['A'].value_counts();
df12['B'].value_counts();
df12['C'].value_counts();
df12['D'].value_counts();
df12['E'].value_counts();
df12['F'].value_counts();





