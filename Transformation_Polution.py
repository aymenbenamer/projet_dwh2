#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 11:25:01 2024

@author: achrafbenamer
"""
import pandas as pd
import os

df_pollutionO3 = pd.read_csv("/Users/achrafbenamer/Desktop/projet_dwh/DATALAKE/Poluant/poluantO3.csv",delimiter=";")
df_pollutionNO2 = pd.read_csv("/Users/achrafbenamer/Desktop/projet_dwh/DATALAKE/Poluant/poluantNO2.csv",delimiter=";")

Missing_values = (df_pollutionNO2.isnull().sum() / len(df_pollutionNO2)) * 100
print("Pourcentage de valeurs manquantes :\n")
print(Missing_values.sort_values(ascending=False))

df_pollution = pd.concat([df_pollutionO3, df_pollutionNO2], ignore_index=True)


# Step 1: Group by the "Polluant" column and count the occurrences
dim_polluant = df_pollution.groupby("Polluant").size().reset_index(name="count")

# Step 2: Insert an "id_pol" column with custom IDs
dim_polluant.insert(0, 'id_pol', ['P' + str(i) for i in range(1, len(dim_polluant) + 1)])

dim_polluant = dim_polluant.drop(
    columns=[
        "count"
    ])

final_data_folder = './final_data'

# S'assurer que le répertoire final_data existe
os.makedirs(final_data_folder, exist_ok=True)

dim_polluant.to_csv(os.path.join(final_data_folder, 'dim_polluant.csv'), index=False)

print(dim_polluant)