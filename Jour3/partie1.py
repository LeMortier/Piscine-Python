import requests

def get_request(url: str) -> (int, str):
    try:
        response = requests.get(url)
        status_code = response.status_code
        json_content = response.json()  # Essaie de convertir la réponse en JSON
        return status_code, json_content
    except requests.exceptions.RequestException as e:
        # Si une erreur réseau se produit, on peut retourner un code d'erreur et le message d'erreur
        print(f"Une erreur s'est produite: {e}")
        return 500, str(e)
    except ValueError:
        # Si le contenu n'est pas en format JSON valide
        print("Le contenu de la réponse n'est pas en format JSON.")
        return response.status_code, "Contenu non-JSON"

# Exemple d'utilisation avec REST Countries API
if __name__ == "__main__":
    url = "https://restcountries.com/v3.1/all"
    status_code, json_content = get_request(url)
    print(f"Code de statut: {status_code}")
    print(f"Contenu JSON: {json_content}")

# partie1.1

import requests

def get_countries_info(country_codes: list, info: list) -> (int, str):
    
    base_url = "https://restcountries.com/v3.1/alpha"
    
    # Joindre les codes pays pour les inclure dans l'URL
    codes = ','.join(country_codes)
    
    # Joindre les informations à récupérer pour les passer en tant que paramètres de requête
    fields = ','.join(info)
    
    # Construire l'URL avec les paramètres de requête
    url = f"{base_url}/{codes}?fields={fields}"

    try:
        # Effectuer la requête GET
        response = requests.get(url)
        
        # Obtenir le code de statut
        status_code = response.status_code
        
        # Obtenir le contenu JSON de la réponse
        json_content = response.json()
        
        return status_code, json_content
    except requests.exceptions.RequestException as e:
        # Gestion des erreurs de requête
        print(f"Une erreur s'est produite: {e}")
        return 500, str(e)
    except ValueError:
        # Gestion des erreurs de conversion en JSON
        print("Le contenu de la réponse n'est pas en format JSON.")
        return response.status_code, "Contenu non-JSON"

# Exemple d'utilisation
if __name__ == "__main__":
    country_codes = ["fr", "us", "jp"]
    info = ["capital", "languages", "population"]
    
    status_code, json_content = get_countries_info(country_codes, info)
    print(f"Code de statut: {status_code}")
    print(f"Contenu JSON: {json_content}")
    
 # partie1.py

import requests

def handle_request_status(url: str) -> int | str:
    try:
        # Effectuer une requête POST sur l'URL
        response = requests.post(url)
        
        # Lever une exception si le statut n'indique pas un succès
        response.raise_for_status()
        
        # Retourner le code de statut si la requête est un succès
        return response.status_code
    except requests.exceptions.HTTPError as http_err:
        # Gérer l'exception en retournant un message d'erreur
        return f"Erreur HTTP: {http_err}"
    except requests.exceptions.RequestException as err:
        # Gérer d'autres exceptions possibles liées à la requête
        return f"Erreur de requête: {err}"

# Exemple d'utilisation
if __name__ == "__main__":
    # Tester avec HTTPBin en simulant différentes réponses de statut
    url = "https://httpbin.org/status/200"  # différentes valeurs possibles comme 404, 500
    result = handle_request_status(url)
    print(result)  # Affichera le code de statut ou l'erreur
   
