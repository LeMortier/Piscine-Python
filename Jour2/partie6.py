import pandas as pd


def pandas_json_read(file: str) -> pd.DataFrame:
   
    return pd.read_json(file)


def pandas_json_write(file: str, data: pd.DataFrame):
   
    data.to_json(file, indent=4, orient="records")

import pandas as pd
import json

def pandas_complex_json(file: str, product: dict):
    # Charger le contenu du fichier JSON dans un DataFrame
    with open(file, 'r') as f:
        data = json.load(f)
    
    df = pd.DataFrame(data['transactions'])

    # 1. Modifier la première transaction pour ajouter un produit
    df.at[0, 'products'].append(product)

    # 2. Supprimer la deuxième transaction (index 1)
    df.drop(index=1, inplace=True)

    # 3. Supprimer le deuxième produit de la troisième transaction
    df.at[2, 'products'].pop(1)

    # Sauvegarder les modifications dans le fichier JSON avec une indentation de 2 espaces
    data['transactions'] = df.to_dict(orient='records')
    with open(file, 'w') as f:
        json.dump(data, f, indent=2)

    