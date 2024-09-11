import requests

def get_companies_with_name(name: str) -> list[dict]:
    # URL de l'API Open Data
    url = "https://api.insee.fr/entreprises/sirene/V3/siren"
    params = {
        'q': f'denominationUniteLegale:{name}',
        'nombre': 10  # Nombre d'entreprises retournées (par défaut 10)
    }
    headers = {
        'Authorization': 'Bearer your_api_key',
        'Accept': 'application/json'
    }
    try:
        # Envoyer la requête HTTP GET à l'API
        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            data = response.json()
            companies = []
            
            # Parcourir les résultats et récupérer les informations nécessaires
            for company in data['unitesLegales']:
                siren = company['siren']
                name = company['periodesUniteLegale'][0]['denominationUniteLegale']
                creation_date = company['periodesUniteLegale'][0]['dateCreationUniteLegale']
                
                companies.append({
                    'SIREN': siren,
                    'Nom complet': name,
                    'Date de création': creation_date
                })
            
            return companies
        else:
            return []
    
    except Exception as e:
        # En cas d'erreur (ex. problème de connexion), retourner une liste vide
        print(f"Erreur: {e}")
        return []

# Exemple 
companies = get_companies_with_name("Boulangerie")
for company in companies:
    print(company)

#second

import requests

def get_all_companies_with_name(name: str) -> list[dict]:
    url = "https://api.insee.fr/entreprises/sirene/V3/siren"  # Exemple d'URL
    headers = {
        'Accept': 'application/json',
        'Authorization': 'Bearer YOUR_ACCESS_TOKEN'  # Remplacer par le token d'accès si requis
    }
    params = {
        'q': name,
        'nombre': 100,  
        'page': 1       
    }

    all_companies = []

    try:
        while True:
            response = requests.get(url, headers=headers, params=params)
            response.raise_for_status()  # Vérifie si la requête a échoué

            # Récupérer les entreprises de la page actuelle
            companies = response.json()

            if not companies.get('etablissement', []):
                break  # Si aucune entreprise n'est trouvée, on arrête la boucle

            # Ajouter les entreprises de cette page à la liste finale
            for company in companies['etablissement']:
                all_companies.append({
                    'SIREN': company.get('siren'),
                    'nom_complet': company.get('nom_complet'),
                    'date_creation': company.get('date_creation')
                })

            # Pagination : on vérifie si on a encore d'autres pages
            total_pages = companies.get('total_pages', 1)  # On cherche le nombre total de pages dans la réponse
            current_page = params['page']

            if current_page >= total_pages:
                break  # Si nous avons tout récupéré, break 

            # Sinon, passer à la page suivante
            params['page'] += 1

        return all_companies

    except (requests.RequestException, ValueError):
        # En cas d'erreur, retourner une liste vide
        return []

# Exemple 
if __name__ == "__main__":
    entreprises = get_all_companies_with_name("EPITECH")
    print(entreprises)

#Third

import csv
import os
from operator import itemgetter

def get_all_companies_with_name(name: str) -> list[dict]:
    """Fonction réutilisée de l'exercice précédent pour récupérer les entreprises."""
    # Code de l'xercice 2 à mettre ici
    pass  # Utiliser la fonction get_all_companies_with_name 

def get_and_store_companies(filename: str, name: str):
    try:
        # 1. Récupérer les entreprises via l'API
        companies = get_all_companies_with_name(name)
        if not companies:
            return  # Si aucune entreprise n'est trouvée ou en cas d'erreur API

        # 2. Lire le fichier existant (si le fichier existe)
        existing_companies = []
        if os.path.exists(filename):
            with open(filename, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    existing_companies.append({
                        'SIREN': row['SIREN'],
                        'nom_complet': row['nom_complet'],
                        'date_creation': row['date_creation']
                    })

        # 3. Fusionner les nouvelles entreprises avec les entreprises existantes
        # On s'assure de ne pas dupliquer les entreprises déjà présentes
        siren_existing = {company['SIREN'] for company in existing_companies}
        new_companies = [c for c in companies if c['SIREN'] not in siren_existing]

        all_companies = existing_companies + new_companies
        # 4. Trier les entreprises par SIREN
        all_companies_sorted = sorted(all_companies, key=itemgetter('SIREN'))
        # 5. Écrire toutes les entreprises dans le fichier (écrasement)
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            fieldnames = ['SIREN', 'nom_complet', 'date_creation']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(all_companies_sorted)

    except Exception as e:
        print(f"Une erreur s'est produite : {e}")

# Exemple
if __name__ == "__main__":
    get_and_store_companies("entreprises.csv", "EPITECH")
