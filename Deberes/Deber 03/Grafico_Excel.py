# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 20:35:51 2020

@author: xavi2
"""
import pandas as pd
import os
import numpy as np
import sqlite3

path_guardado = "C://Users//xavi2//Documents//GitHub//py-iniguez-sarango-rodman-xavier//Deberes//Deber 03//data//artwork_data.pickle"

df =  pd.read_pickle(path_guardado)

sub_df = df.iloc[49980:50519,:].copy()

# Excel
path_excel = "C://Users//xavi2//Documents//GitHub//py-iniguez-sarango-rodman-xavier//Deberes//Deber 03//data//Excel_artwork_data.xlsx"

num_artistas = sub_df['artist'].value_counts()

writer = pd.ExcelWriter(path_excel,engine='xlsxwriter')

num_artistas.to_excel(writer,sheet_name='Artista')
workbook = writer.book
worksheet = writer.sheets['Artista']

chart = workbook.add_chart({'type': 'column','name':'Artista'})
chart.add_series({
    'name': '=Artista!B1',
    'values':     '=Artista!$B$2:$B$30',
    'categories': '=Artista!$A$2:$A$30',
    'gap':        30,
    'data_labels': {'value': True}
})
chart.set_title({'name': 'Obras por artista'})
chart.set_legend({'none': True})
chart.set_style(4)
chart.set_x_axis({
    'name': 'Artistas',
    'num_font': {
        'name': 'Arial Narrow',
        'color': '#000000',
    },
})

chart.set_y_axis({
    'name': '# Obras',
    'num_font': {
        'name': 'Arial Narrow',
        'color': '#000000',
    },
})
worksheet.insert_chart('D3', chart, {'x_scale': 1.5, 'y_scale': 1.5})
writer.save()