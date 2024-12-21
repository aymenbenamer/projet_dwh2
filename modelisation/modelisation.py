import pandas as pd
from sqlalchemy import create_engine, text

# Configuration de la base de données PostgreSQL
DATABASE_URI = 'postgresql://postgres:    @localhost:5432/projet_dwh'
engine = create_engine(DATABASE_URI)

# Connexion à la base de données
with engine.connect() as connection:
    # 1. Création de la table dim_ville
    connection.execute(text("""
        CREATE TABLE IF NOT EXISTS dim_commune (
            id_commune INT PRIMARY KEY,
            code_postale INT,
            nom_ville VARCHAR(255)
        );
    """))

    # 4. Création de la table fact_population
    connection.execute(text("""
        CREATE TABLE IF NOT EXISTS fact_population (
            id_commune INT,
            nb_population FLOAT,
            nb_logement FLOAT,
            nb_constructions FLOAT,
            nb_entreprise FLOAT,
            densite_population FLOAT,
            FOREIGN KEY (id_commune) REFERENCES dim_commune(id_commune)
        );
    """))
    connection.execute(text("""
        CREATE TABLE IF NOT EXISTS dim_transport (
            id_transport INT PRIMARY KEY,
            id_commune INT,
            mode VARCHAR(255),
            count INT
        );
    """))
    connection.execute(text("""
        CREATE TABLE IF NOT EXISTS dim_polluant (
            id_pol varchar(255) PRIMARY KEY,
            Polluant VARCHAR(255)
        );
    """))


# Charger les fichiers CSV
dim_commune = pd.read_csv('/Users/achrafbenamer/Desktop/projet_dwh/final_data/dim_commune.csv', delimiter=',')
fact_population = pd.read_csv('/Users/achrafbenamer/Desktop/projet_dwh/final_data/fact_population.csv', delimiter=',')
dim_transport = pd.read_csv('/Users/achrafbenamer/Desktop/projet_dwh/final_data/dim_transport.csv', delimiter=',')
dim_polluant =  pd.read_csv('/Users/achrafbenamer/Desktop/projet_dwh/final_data/dim_polluant.csv', delimiter=',')
dim_time =  pd.read_csv('/Users/achrafbenamer/Desktop/projet_dwh/final_data/dim_time.csv', delimiter=',')
fact_table_pol = pd.read_csv('/Users/achrafbenamer/Desktop/projet_dwh/final_data/fact_table_pol.csv', delimiter=',')



# Connexion à la base de données pour insérer les données
with engine.connect() as connection:
    # 5. Insérer les données dans la table dim_ville
    """dim_commune.to_sql('dim_commune', engine, if_exists='replace', index=False)
    # 8. Insérer les données dans la table fact_population
    fact_population.to_sql('fact_population', engine, if_exists='replace', index=False)
    dim_transport.to_sql('dim_transport', engine, if_exists='replace', index=False)
    dim_polluant.to_sql('dim_polluant', engine, if_exists='replace', index=False)
    dim_time.to_sql('dim_time', engine, if_exists='replace', index=False)
    fact_table_pol.to_sql('fact_table_pol', engine, if_exists='replace', index=False)"""
    
    
    
print("Les tables ont été créées et les données ont été insérées avec succès dans PostgreSQL.")
