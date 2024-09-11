#exo1
import pandas as pd

def create_multi_index_df(df: pd.DataFrame) -> pd.DataFrame:
    # Définir l'index avec 'year' et 'region'
    df_multi_index = df.set_index(['year', 'region'])
    
    # Trier le DataFrame par l'index
    df_multi_index = df_multi_index.sort_index()
    
    return df_multi_index

# Charger le fichier CSV
sales_df = pd.read_csv('C:\\Users\\Matthieu\\Desktop\\Piscine Python\\Jour6\\sales.csv')

# Créer le DataFrame 
multi_index_df = create_multi_index_df(sales_df)

# Verif
print(multi_index_df.head())

 
#exo2
import pandas as pd

def retrieve_multi_index_data(df: pd.DataFrame, year: int, region: str) -> pd.DataFrame:
    """
    Cette fonction récupère les données d'un DataFrame multi-indexé en fonction de l'année et de la région spécifiées.
    
    :param df: DataFrame multi-indexé
    :param year: Année à filtrer
    :param region: Région à filtrer
    :return: DataFrame filtré pour l'année et la région spécifiées
    """
    try:
        # Utilisation de la sélection par index avec .loc pour récupérer les données spécifiques
        return df.loc[(year, region)]
    except KeyError:
        print(f"Aucune donnée trouvée pour l'année {year} et la région {region}.")
        return pd.DataFrame()

# fichier CSV
file_path = 'C:\\Users\\Matthieu\\Desktop\\Piscine Python\\Jour6\\sales.csv' 
sales_df = pd.read_csv(file_path)

# DataFrame multi-indexé par 'year' et 'region'
sales_df.set_index(['year', 'region'], inplace=True)
sales_df.sort_index(inplace=True)

#'année et la région à filtrer
year = 2003
region = 'EMEA'

# Récupérer les données pour l'année et la région spécifiques
filtered_data = retrieve_multi_index_data(sales_df, year, region)

print(f"Données filtrées pour l'année {year} et la région {region} :")
print(filtered_data)

import pandas as pd

# Exo3
def multi_index_aggregate(df: pd.DataFrame) -> pd.DataFrame:
   
    # Agréger les données par année et région
    agg_df = df.groupby(['year', 'region']).agg(
        total_quantity=('quantity', 'sum'),
        total_sales=('total_price', 'sum')
    )
    
    # Arrondir les résultats à deux décimales
    agg_df = agg_df.round(2)
    
    return agg_df

# fichier CSV
file_path = 'C:\\Users\\Matthieu\\Desktop\\Piscine Python\\Jour6\\sales.csv'  
sales_df = pd.read_csv(file_path)

sales_df.set_index(['year', 'region'], inplace=True)
sales_df.sort_index(inplace=True)

# fonction d'agrégation
aggregated_data = multi_index_aggregate(sales_df)

# résultats
print("Données agrégées par année et région :")
print(aggregated_data)

# Exo4
import pandas as pd

def columns_multi_index(df: pd.DataFrame) -> pd.DataFrame:
   
    # Agréger les données par année, région et catégorie
    agg_df = df.groupby(['year', 'region', 'category']).agg(
        total_quantity=('quantity', 'sum'),
        total_sales=('total_price', 'sum')
    )
    
    # Arrondir les résultats à deux décimales
    agg_df = agg_df.round(2)
    
    # Réorganiser pour avoir un pivot avec la catégorie dans les colonnes
    pivot_df = agg_df.unstack(level='category')
    
    return pivot_df

# fichier CSV
file_path = 'C:\\Users\\Matthieu\\Desktop\\Piscine Python\\Jour6\\sales.csv'  
sales_df = pd.read_csv(file_path)

sales_df.set_index(['year', 'region', 'category'], inplace=True)
sales_df.sort_index(inplace=True)

# création des fonction multi indexées
columns_multi_indexed_df = columns_multi_index(sales_df)

# résultats
print("Données avec colonnes multi-indexées :")
print(columns_multi_indexed_df)

#Exo5

import pandas as pd

def swap_columns_multi_index(df: pd.DataFrame) -> pd.DataFrame:
    # inverse les niveaux des colonnes 
    df_swapped = df.swaplevel(axis=1)
    
    # regrouper les informations par catégorie
    df_swapped = df_swapped.sort_index(axis=1)
    
    return df_swapped

# fichier CSV
file_path = 'C:\\Users\\Matthieu\\Desktop\\Piscine Python\\Jour6\\sales.csv' 
sales_df = pd.read_csv(file_path)

sales_df.set_index(['year', 'region', 'category'], inplace=True)
sales_df.sort_index(inplace=True)

# calculs d'agrégation de l'exo 4
def columns_multi_index(df: pd.DataFrame) -> pd.DataFrame:
    agg_df = df.groupby(['year', 'region', 'category']).agg(
        total_quantity=('quantity', 'sum'),
        total_sales=('total_price', 'sum')
    )
    agg_df = agg_df.round(2)
    return agg_df.unstack(level='category')

# calcul des données agrégées avec colonnes multi-indexées
columns_multi_indexed_df = columns_multi_index(sales_df)

# nverse les colonnes avec swap_columns_multi_index 
swapped_columns_df = swap_columns_multi_index(columns_multi_indexed_df)

# Afficher les résultats
print("Données avec colonnes inversées :")
print(swapped_columns_df)

#Exo6

import pandas as pd

# Exercice 6 : Récupération de colonnes et lignes Multi-Indexées

# Fonction 1 : Récupérer uniquement les données pour une catégorie donnée
def retrieve_multi_index_column(df: pd.DataFrame, category: str) -> pd.DataFrame:
    # Utiliser .xs pour sélectionner une colonne spécifique dans un multi-index
    return df.xs(key=category, axis=1, level='category')

# Fonction 2 : Récupérer les données pour une catégorie et une année données
def retrieve_multi_index_basic(df: pd.DataFrame, category: str, year: int) -> pd.DataFrame:
    # Utiliser .loc pour filtrer par année et xs pour la catégorie
    filtered_df = df.loc[year]
    return filtered_df.xs(key=category, axis=1, level='category')

# Fonction 3 : Récupérer les données pour une région et une sous-colonne donnée
def retrieve_multi_index_advanced(df: pd.DataFrame, region: str, sub_column: str) -> pd.DataFrame:
    # Utiliser .xs pour sélectionner par région et sous-colonne
    return df.xs(key=region, axis=0, level='region')[sub_column]

# Charger le fichier CSV
file_path = 'C:\\Users\\Matthieu\\Desktop\\Piscine Python\\Jour6\\sales.csv'  
sales_df = pd.read_csv(file_path)

sales_df.set_index(['year', 'region', 'category'], inplace=True)
sales_df.sort_index(inplace=True)

# Applique les calculs d'agrégation de l'exo 4
def columns_multi_index(df: pd.DataFrame) -> pd.DataFrame:
    agg_df = df.groupby(['year', 'region', 'category']).agg(
        total_quantity=('quantity', 'sum'),
        total_sales=('total_price', 'sum')
    )
    agg_df = agg_df.round(2)
    return agg_df.unstack(level='category')

# colonnes multi-indexées
columns_multi_indexed_df = columns_multi_index(sales_df)

# Exemples :

# Fonction 1 : Récupérer les données pour une catégorie donnée
category_data = retrieve_multi_index_column(columns_multi_indexed_df, 'Electronics')
print("Données pour la catégorie 'Electronics' :")
print(category_data)

# Fonction 2 : Récupérer les données pour une catégorie et une année données
category_year_data = retrieve_multi_index_basic(columns_multi_indexed_df, 'Electronics', 2022)
print("\nDonnées pour la catégorie 'Electronics' en 2022 :")
print(category_year_data)

# Fonction 3 : Récupérer les données pour une région et une sous-colonne donnée
region_column_data = retrieve_multi_index_advanced(columns_multi_indexed_df, 'North', 'total_sales')
print("\nDonnées de 'total_sales' pour la région 'North' :")
print(region_column_data)
 