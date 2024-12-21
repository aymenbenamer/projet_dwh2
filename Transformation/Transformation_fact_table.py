#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 16:27:16 2024

@author: achrafbenamer

"""

import pandas as pd
from Transformation_Polution import df_pollutionO3,df_pollutionNO2
from Transformation_Polution import dim_polluant
from Transformation_Time import dim_time
import os 



df_pollution = pd.concat([df_pollutionO3, df_pollutionNO2], ignore_index=True)

# Convertir les colonnes 'Date de début' et 'date' en datetime
df_pollution['Date de début'] = pd.to_datetime(df_pollution['Date de début'])
dim_time['Date de début'] = pd.to_datetime(dim_time['Date de début'])
 
# Associer id_polluant à df_NO2_O3
fact_table = df_pollution.merge(dim_polluant, left_on='Polluant', right_on='Polluant', how='left')
 
# Associer id_time en utilisant les dates
fact_table = fact_table.merge(dim_time[['id_time', 'Date de début']], left_on='Date de début', right_on='Date de début', how='left')
 
# Ajouter id_commune (fixé à 'C1' dans cet exemple)
fact_table['id_commune'] = 1
 
# Conserver uniquement les colonnes nécessaires
fact_table = fact_table[['id_commune', 'id_time', 'id_pol', 'valeur']]

print(fact_table)

final_data_folder = '/Users/achrafbenamer/Desktop/projet_dwh/final_data'

# S'assurer que le répertoire final_data existe
os.makedirs(final_data_folder, exist_ok=True)

fact_table.to_csv(os.path.join(final_data_folder, 'fact_table_pol.csv'), index=False)

print(dim_polluant)