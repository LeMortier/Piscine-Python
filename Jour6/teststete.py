import pandas as pd

def create_multi_index_df(df: pd.DataFrame) -> pd.DataFrame:
    # Convertir la colonne 'orderDate' en datetime
    df['orderDate'] = pd.to_datetime(df['orderDate'])
    
    # Extraire l'année de la colonne 'orderDate'
    df['year'] = df['orderDate'].dt.year
    
    # Créer un DataFrame multi-indexé par 'year' et 'region'
    multi_index_df = df.set_index(['year', 'region']).sort_index()
    
    return multi_index_df

#exo 1 p2 arch
#exo1
import pandas as pd

# Charger le fichier CSV
df = pd.read_csv('C:\\Users\\Matthieu\\Desktop\\Piscine Python\\Jour6\\sales.csv')

# Afficher un aperçu des premières lignes du DataFrame
print(df.head())
 
 
import pandas as pd

# Exercice 1 : Création du DataFrame Multi-Indexé
def create_multi_index_df(df: pd.DataFrame) -> pd.DataFrame:
    # Définir l'index multi-niveau avec 'year' et 'region'
    df_multi_index = df.set_index(['year', 'region'])
    
    # Trier le DataFrame par l'index pour un accès efficace
    df_multi_index = df_multi_index.sort_index()
    
    return df_multi_index

# Exercice 2 : Récupération de données Multi-Indexées
def retrieve_multi_index_data(df: pd.DataFrame, year: int, region: str) -> pd.DataFrame:
    # Utilisation de la sélection par index avec .loc pour récupérer les données spécifiques
    return df.loc[(year, region)]

# Charger le fichier CSV
file_path = 'C:\\Users\\Matthieu\\Desktop\\Piscine Python\\Jour6\\sales.csv'  # Assurez-vous que le fichier CSV est dans le même répertoire ou fournissez un chemin correct
sales_df = pd.read_csv(file_path)

# Créer le DataFrame multi-indexé (Exercice 1)
multi_index_df = create_multi_index_df(sales_df)

# Spécifier l'année et la région à filtrer (par exemple 2003 et 'EMEA')
year = 2003
region = 'EMEA'

# Récupérer les données pour l'année et la région spécifiques (Exercice 2)
filtered_data = retrieve_multi_index_data(multi_index_df, year, region)

# Afficher les résultats
print("Données filtrées pour l'année", year, "et la région", region)
print(filtered_data)
 
