from pymongo import MongoClient

def get_mongo_client(host: str, port: int) -> MongoClient:
  
    try:
        # Création du client MongoDB 
        client = MongoClient(host, port)
        # Optionnel : Tester la connexion en accédant à la liste des bases de données
        client.admin.command('ping')
        print("Connexion réussie à MongoDB")
        return client
    except Exception as e:
        print(f"Erreur de connexion : {e}")
        return None

# Exemple 
if __name__ == "__main__":
    host = "localhost"  
    port = 27017        
    client = get_mongo_client(host, port)
    
from pymongo import MongoClient

def get_all_laureates(client: MongoClient) -> list[dict]:
   
    try:
        # Accéder à la base de données "nobel" et à la collection "laureates"
        db = client["nobel"]
        collection = db["laureates"]

        # Récupérer les documents
        laureates = list(collection.find())

        print(f"{len(laureates)} lauréats récupérés.")
        return laureates

    except Exception as e:
        print(f"Erreur lors de la récupération des lauréats : {e}")
        return []

# Exemple 
if __name__ == "__main__":
    host = "localhost"
    port = 27017
    client = MongoClient(host, port)

    laureates = get_all_laureates(client)
    for laureate in laureates[:5]:  
        print(laureate)
    
from pymongo import MongoClient

# Fonction pour se connecter à la base de données MongoDB
def get_mongo_client(host: str, port: int) -> MongoClient:
    return MongoClient(host, port)

# Exercice 3.1 : Récupérer les informations des lauréats
def get_laureates_information(client: MongoClient) -> list[dict]:
    db = client.nobel  # Connexion à la base de données 'nobel'
    collection = db.laureates  # Connexion à la collection 'laureates'
    
    # Requête pour récupérer les noms, prénoms et date de naissance des lauréats
    laureates_info = collection.find({}, {"firstname": 1, "surname": 1, "born": 1, "_id": 0})
    
    # Conversion des résultats en liste de dictionnaires
    return list(laureates_info)

# Exercice 3.2 : Récupérer les catégories de prix Nobel
def get_prize_categories(client: MongoClient) -> list[str]:
    db = client.nobel  # Connexion à la base de données 'nobel'
    collection = db.laureates  # Connexion à la collection 'laureates'
    
    # Utilisation de 'distinct' pour récupérer les catégories uniques
    categories = collection.distinct("category")
    
    return categories

# Exemple
if __name__ == "__main__":
    client = get_mongo_client('localhost', 27017)
    
    # Récupération des informations des lauréats
    laureates = get_laureates_information(client)
    for i in range(2):  # Affiche les informations des deux premiers lauréats
        print(laureates[i])
    
    categories = get_prize_categories(client)
    print(categories)

from pymongo import MongoClient
import re

# Fonction pour se connecter à la base de données MongoDB
def get_mongo_client(host: str, port: int) -> MongoClient:
    return MongoClient(host, port)

# Exercice 4.1 : Récupérer les lauréats par catégorie
def get_category_laureates(client: MongoClient, category: str) -> list[dict]:
    db = client.nobel  # Connexion à la base de données 'nobel'
    collection = db.laureates  # Connexion à la collection 'laureates'
    # Requête pour récupérer les lauréats d'une catégorie 
    laureates = collection.find({"category": category}, {"firstname": 1, "surname": 1, "category": 1, "_id": 0})
    # Conversion des résultats en liste de dictionnaires
    return list(laureates)

# Exercice 4.2 : Récupérer les lauréats par pays de naissance
def get_country_laureates(client: MongoClient, country: str) -> list[dict]:
    db = client.nobel  # Connexion à la base de données 'nobel'
    collection = db.laureates  # Connexion à la collection 'laureates'
    # Utilisation d'une regex pour gérer les pays actuels et anciens
    country_regex = re.compile(country, re.IGNORECASE)
    # Requête pour récupérer les lauréats nés dans un pays donné (ou ancien pays)
    laureates = collection.find({"bornCountry": country_regex}, {"firstname": 1, "surname": 1, "bornCountry": 1, "_id": 0})
    # Conversion des résultats en liste de dictionnaires
    return list(laureates)

# Exemple 
if __name__ == "__main__":
    client = get_mongo_client('localhost', 27017)
    # Récupération des lauréats par catégorie 
    category_laureates = get_category_laureates(client, "physics")
    for i in range(2):  # Affiche les deux premiers 
        print(category_laureates[i])
    # Récupération des lauréats par pays 
    country_laureates = get_country_laureates(client, "Poland")
    for i in range(2):  # Affiche les deux premiers 
        print(country_laureates[i])

from pymongo import MongoClient

# Fonction pour se connecter à la base de données MongoDB
def get_mongo_client(host: str, port: int) -> MongoClient:
    return MongoClient(host, port)

# Exercice 5.1 : Récupérer tous les prix Nobel partagés entre plusieurs lauréats
def get_shared_prizes(client: MongoClient) -> list[dict]:
    db = client.nobel  # Connexion à la base de données 'nobel'
    collection = db.prizes  # Connexion à la collection 'prizes'
    
    # Requête pour récupérer les prix partagés par plusieurs lauréats
    shared_prizes = collection.find(
        {"laureates.1": {"$exists": True}},  # Vérifie qu'il y a plus d'un lauréat pour un prix
        {"year": 1, "category": 1, "laureates": 1, "_id": 0}  # Sélection des champs à afficher
    )
    
    # Conversion des résultats en liste de dictionnaires
    return list(shared_prizes)

# Exercice 5.2 : Récupérer les prix Nobel partagés exactement entre 2 personnes pour la même motivation
def get_shared_prizes_common(client: MongoClient) -> list[dict]:
    db = client.nobel  # Connexion à la base de données 'nobel'
    collection = db.prizes  # Connexion à la collection 'prizes'
    
    # Requête pour récupérer les prix partagés entre exactement 2 personnes, même motivation
    shared_prizes_common = collection.find(
        {
            "$and": [
                {"laureates": {"$size": 2}},  # Vérifie qu'il y a exactement 2 lauréats
                {"laureates.0.motivation": {"$exists": True}},  # Vérifie que la motivation existe
                {"laureates.1.motivation": {"$exists": True}},
                {"$expr": {"$eq": ["$laureates.0.motivation", "$laureates.1.motivation"]}}  # Vérifie que les motivations sont identiques
            ]
        },
        {"year": 1, "category": 1, "laureates": 1, "_id": 0}  # Sélection des champs à afficher
    )
    
    # Conversion des résultats en liste de dictionnaires
    return list(shared_prizes_common)

# Exemple 
if __name__ == "__main__":
    client = get_mongo_client('localhost', 27017)
    
    # Récupérer tous les prix Nobel partagés
    shared_prizes = get_shared_prizes(client)
    for i in range(2):  # Affiche les deux premiers résultats
        print(shared_prizes[i])
    
    # Récupérer les prix Nobel partagés exactement entre 2 personnes avec même motivation
    shared_prizes_common = get_shared_prizes_common(client)
    for i in range(2):  # Affiche les deux premiers résultats
        print(shared_prizes_common[i])
