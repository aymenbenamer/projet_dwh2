#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 11:19:27 2024

@author: achrafbenamer
"""

import pandas as pd
import os

df_arret_lignes = pd.read_csv("/Users/achrafbenamer/Desktop/projet_dwh/DATALAKE/Transport/arret.csv")

df_arret_lignes.head(5)

Missing_values = (df_arret_lignes.isnull().sum() / len(df_arret_lignes)) * 100
print("Pourcentage de valeurs manquantes :\n")
print(Missing_values.sort_values(ascending=False))

duplicates = df_arret_lignes["mode"].duplicated()
duplicates.sum()

df_arret_lignes = df_arret_lignes.drop_duplicates(subset=["shortName"], keep="first")


df_arret_lignes = df_arret_lignes.groupby("mode").size().reset_index(name="Count")

dim_transport = df_arret_lignes

dim_transport["id_commune"] = 1

dim_transport.insert(0, 'id_transport', [str(i) for i in range(1, len(dim_transport) + 1)])


final_data_folder = './final_data'

# S'assurer que le répertoire final_data existe
os.makedirs(final_data_folder, exist_ok=True)

dim_transport.to_csv(os.path.join(final_data_folder, 'dim_transport.csv'), index=False)

dim_transport
