#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 13:01:07 2024

@author: achrafbenamer
"""

import pandas as pd
import os 

from Transformation_Polution import df_pollution

df_pollution["Date de début"]=pd.to_datetime(df_pollution['Date de début']).dt.normalize()



dim_time = df_pollution[["Date de début"]]

dim_time = dim_time.rename(columns={'"Date de début"': 'date'})


dim_time = dim_time.drop_duplicates(subset=['Date de début'])

dim_time.insert(0, 'id_time', [str(i) for i in range(1, len(dim_time) + 1)])


dim_time["month"] = dim_time["Date de début"].dt.month
dim_time["year"] = dim_time["Date de début"].dt.year
dim_time["quarter"] = dim_time["Date de début"].dt.quarter

print(dim_time)

final_data_folder = '/Users/achrafbenamer/Desktop/projet_dwh/final_data'

# S'assurer que le répertoire final_data existe
os.makedirs(final_data_folder, exist_ok=True)

dim_time.to_csv(os.path.join(final_data_folder, 'dim_time.csv'), index=False)
