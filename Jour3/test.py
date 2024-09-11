# partie1.py

import requests

def handle_request_status(url: str) -> int | str:
    """
    Effectue une requête POST sur l'URL donnée et retourne le code de statut si la requête réussit.
    Si la requête échoue, retourne l'exception sous forme de chaîne de caractères.

    :param url: L'URL sur laquelle effectuer la requête POST.
    :return: Le code de statut si succès, ou un message d'exception en cas d'échec.
    """
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
    url = "https://httpbin.org/status/200"  # Vous pouvez essayer différentes valeurs comme 404, 500
    result = handle_request_status(url)
    print(result)  # Affichera le code de statut ou l'erreur
