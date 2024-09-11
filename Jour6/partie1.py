# exo1

import pandas as pd
file =r'C:\Users\Matthieu\Desktop\Piscine Python\Jour6\flights.parquet'

def read_parquet(filename: str) -> pd.DataFrame:
    # Charger le fichier Parquet dans un DataFrame
    df = pd.read_parquet(filename)
    # Retourner les 10 premières lignes du DataFrame
    result = df.head(10)
    # Imprimer le résultat dans le terminal
    # Retourner le DataFrame
    return result

result = read_parquet(file)
print(result)

#exo2

import pandas as pd
file =r'C:\Users\Matthieu\Desktop\Piscine Python\Jour6\flights.parquet'
def read_parquet_columns(filename: str, columns: list) -> pd.DataFrame:
    # Charger uniquement les colonnes spécifiées dans un DataFrame
    df = pd.read_parquet(filename, columns=columns)
    # Retourner le DataFrame avec les colonnes spécifiques
    return df

result = read_parquet(file)
print(result)

#exo3

import pyarrow.parquet as pq
import pandas as pd
file =r'C:\Users\Matthieu\Desktop\Piscine Python\Jour6\flights.parquet'
def read_parquet_batch(filename: str, batch_size: int) -> pd.DataFrame:
    # Ouvrir le fichier Parquet avec PyArrow
    parquet_file = pq.ParquetFile(filename)
    
    # Initialiser un DataFrame vide pour stocker les résultats
    result_df = pd.DataFrame()
    
    # Itérer batchs
    for batch in parquet_file.iter_batches(batch_size=batch_size):
        # Convertir le batch en DataFrame Pandas
        batch_df = batch.to_pandas()
        
        # Ajouter les deux premières lignes du batch au DataFrame final
        result_df = pd.concat([result_df, batch_df.head(2)], ignore_index=True)
    
    # Retourner le DataFrame final
    return result_df
# print le résultat final
result = read_parquet(file)
print(result)


