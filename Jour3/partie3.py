import requests
from bs4 import BeautifulSoup

def find_links_in_paragraphs(url: str) -> list[str]:
  
    try:
        # Faire une requête GET vers l'URL
        response = requests.get(url)
        # Vérifier 
        response.raise_for_status()
        
        # Analyser le contenu HTML de la réponse avec BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Trouver les paragraphes
        paragraphs = soup.find_all('p')
        
        # Extraire les liens
        links = []
        for p in paragraphs:
            for a in p.find_all('a', href=True):
                links.append(a['href'])
        
        return links
    
    except requests.exceptions.RequestException as e:
        # En cas d'erreur, lever une exception 
        raise Exception(f"Une erreur est survenue : {e}")

# Exemple
if __name__ == "__main__":
    url = "https://fr.wikipedia.org/wiki/Cam%C3%A9l%C3%A9on"
    links = find_links_in_paragraphs(url)
    for link in links:
        print(link)

import requests
from bs4 import BeautifulSoup

def fetch_html(url: str) -> BeautifulSoup:
 
    try:
        response = requests.get(url)
        response.raise_for_status()
        return BeautifulSoup(response.content, 'html.parser')
    except requests.exceptions.RequestException as e:
        raise Exception(f"Erreur lors de la requête : {e}")

def recursive_navigation(url: str, nb: int) -> list[str]:
   
    base_url = "https://fr.wikipedia.org"
    visited_links = []

    while nb >= 0:
        # Récupérer le contenu de la page actuelle
        soup = fetch_html(url)
        
        # Trouver tous les paragraphes
        paragraphs = soup.find_all('p')
        
        # Rechercher les liens internes vers Wikipedia dans les paragraphes
        wiki_links = []
        for p in paragraphs:
            for a in p.find_all('a', href=True):
                if a['href'].startswith('/wiki'):
                    wiki_links.append(a['href'])
        
        # Si on a assez de liens pour suivre le nb-ième lien
        if len(wiki_links) > nb:
            next_link = wiki_links[nb]
            full_next_link = base_url + next_link
            visited_links.append(full_next_link)
            
            # Décrémenter `nb` et mettre à jour `url`
            url = full_next_link
            nb -= 1
        else:
            # Si pas assez de liens, arrêter la récursion
            break
    
    return visited_links

# Exemple 
if __name__ == "__main__":
    start_url = "https://fr.wikipedia.org/wiki/Cam%C3%A9l%C3%A9on"
    result_links = recursive_navigation(start_url, 2)
   
    for link in result_links:
        print(link)  

