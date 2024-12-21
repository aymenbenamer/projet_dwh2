import pandas as pd
import os

# Charger le fichier trans_population.csv
trans_population = pd.read_csv('/Users/achrafbenamer/Desktop/projet_dwh/DATALAKE/Demographie/population 1.csv',delimiter=",")

# Vérifier les colonnes du DataFrame
print("Colonnes du DataFrame : ", trans_population.columns)

# Extraire les données nécessaires pour la table dimVille
dim_commune = trans_population[['code_postale', 'nom_ville']]
dim_commune['id_commune'] = 1  # Assigner un ID unique à Versailles (id_ville = 1)
dim_commune = dim_commune[['id_commune', 'code_postale', 'nom_ville']]


# Extraire les données nécessaires pour la table factPopulation
fact_population_data = trans_population[['nb_population', 'nb_logement', 'nb_constructions', 'nb_entreprise', 'densite_population']].iloc[0]
fact_population_data = pd.DataFrame([fact_population_data], columns=['nb_population', 'nb_logement', 'nb_constructions', 'nb_entreprise', 'densite_population'])
fact_population_data['id_commune'] = 1  # Associer Versailles (id_ville = 1)
fact_population_data = fact_population_data[['id_commune', 'nb_population', 'nb_logement', 'nb_constructions', 'nb_entreprise', 'densite_population']]

# Spécifier le répertoire final_data
final_data_folder = '/Users/achrafbenamer/Desktop/projet_dwh/final_data'

# S'assurer que le répertoire final_data existe
os.makedirs(final_data_folder, exist_ok=True)

# Sauvegarder les résultats sous forme de CSV dans le répertoire final_data
dim_commune.to_csv(os.path.join(final_data_folder, 'dim_commune.csv'), index=False)
fact_population_data.to_csv(os.path.join(final_data_folder, 'fact_population.csv'), index=False)

print("Les fichiers ont été sauvegardés dans le répertoire 'final_data'.")