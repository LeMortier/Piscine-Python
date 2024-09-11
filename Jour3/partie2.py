# partie2,0.py

from bs4 import BeautifulSoup

def create_bs_obj(file: str) -> BeautifulSoup:
    try:
        # Ouvrir le fichier HTML 
        with open(file, 'r', encoding='utf-8') as html_file:
            content = html_file.read()
            # Créer et retourner l'objet BS4 à partir du contenu
            soup = BeautifulSoup(content, 'html.parser')
            return soup
    except FileNotFoundError:
        print(f"Erreur : Le fichier {file} est introuvable.")
        return None

if __name__ == "__main__":
    file_path = "Jour3\example.html"
    soup_obj = create_bs_obj(file_path)
    
    if soup_obj:
        print("Titre de la page:", soup_obj.title.string)

        # Extraire tous les paragraphes
        print("\nTous les paragraphes :")
        for p in soup_obj.find_all('p'):
            print(p.text)

        # Extraire tous les liens
        print("\nTous les liens :")
        for link in soup_obj.find_all('a'):
            print(f"Texte : {link.text}, URL : {link['href']}")
        
        # Extraire tout contenu avec la classe 'info'
        print("\nContenu avec la classe 'info' :")
        for info in soup_obj.select('.info'):
            print(info.text)

        # Extraire les données du tableau
        print("\nDonnées du tableau :")
        table = soup_obj.find('table')
        rows = table.find_all('tr')
        for row in rows:
            cols = row.find_all('td')
            cols = [col.text for col in cols]
            print(cols)

# partie2,1.py

from bs4 import BeautifulSoup

def create_bs_obj(file: str) -> BeautifulSoup:
    
    try:
        with open(file, 'r', encoding='utf-8') as html_file:
            content = html_file.read()
            soup = BeautifulSoup(content, 'html.parser')
            return soup
    except FileNotFoundError:
        print(f"Erreur : Le fichier {file} est introuvable.")
        return None

def find_title(file: str) -> str:
    
    soup = create_bs_obj(file)
    if soup:
        title_tag = soup.title
        if title_tag:
            return str(title_tag.string)  
        else:
            return "Aucun titre trouvé."
    return "Erreur lors du chargement de la page."

# Exemple 
if __name__ == "__main__":
    file_path = "Jour3\example.html"  
    title = find_title(file_path)
    print(f"Titre de la page : {title}")

# partie2,2.py

from bs4 import BeautifulSoup

def create_bs_obj(file: str) -> BeautifulSoup:
    
    try:
        with open(file, 'r', encoding='utf-8') as html_file:
            content = html_file.read()
            soup = BeautifulSoup(content, 'html.parser')
            return soup
    except FileNotFoundError:
        print(f"Erreur : Le fichier {file} est introuvable.")
        return None

def find_paragraphs(file: str) -> list[str]:
    
    soup = create_bs_obj(file)
    if soup:
        paragraphs = soup.find_all('p')
        return [str(paragraph.text) for paragraph in paragraphs]  
    return []

# Exemple 
if __name__ == "__main__":
    file_path = "Jour3\example.html"  
    paragraphs = find_paragraphs(file_path)
    print("Paragraphes trouvés :")
    for p in paragraphs:
        print(p)

# partie2,3.py

from bs4 import BeautifulSoup

def create_bs_obj(file: str) -> BeautifulSoup:
    
    try:
        with open(file, 'r', encoding='utf-8') as html_file:
            content = html_file.read()
            soup = BeautifulSoup(content, 'html.parser')
            return soup
    except FileNotFoundError:
        print(f"Erreur : Le fichier {file} est introuvable.")
        return None

def find_links(file: str) -> list[str]:
    
    soup = create_bs_obj(file)
    if soup:
        # Trouver toutes les balises <a> et extraire les attributs href
        links = soup.find_all('a')
        return [link.get('href') for link in links if link.get('href')]  # Extraire les liens (href)
    return []

# Exemple 
if __name__ == "__main__":
    file_path = "Jour3\example.html"  
    links = find_links(file_path)
    print("Liens trouvés :")
    for link in links:
        print(link)

# partie2,4.py

from bs4 import BeautifulSoup

def create_bs_obj(file: str) -> BeautifulSoup:
   
    try:
        with open(file, 'r', encoding='utf-8') as html_file:
            content = html_file.read()
            soup = BeautifulSoup(content, 'html.parser')
            return soup
    except FileNotFoundError:
        print(f"Erreur : Le fichier {file} est introuvable.")
        return None

def find_elements_with_css_class(file: str, class_name: str) -> list[str]:
    
    soup = create_bs_obj(file)
    if soup:
        # Trouver toutes les balises qui ont la classe donnée
        elements = soup.find_all(class_=class_name)
        # Convertir chaque élément en chaîne de caractères
        return [str(element) for element in elements]
    return []

# Exemple 
if __name__ == "__main__":
    file_path = "Jour3\example.html"  
    class_to_find = "info"  # Classe CSS 
    elements = find_elements_with_css_class(file_path, class_to_find)
    print("Éléments trouvés avec la classe CSS 'info' :")
    for element in elements:
        print(element)

# partie2,5.py

import re
from bs4 import BeautifulSoup

def create_bs_obj(file: str) -> BeautifulSoup:
   
    try:
        with open(file, 'r', encoding='utf-8') as html_file:
            content = html_file.read()
            soup = BeautifulSoup(content, 'html.parser')
            return soup
    except FileNotFoundError:
        print(f"Erreur : Le fichier {file} est introuvable.")
        return None

def find_headers(file: str) -> list[str]:
    
    soup = create_bs_obj(file)
    if soup:
        # Utiliser une regex pour trouver toutes les balises d'en-tête <h1>, <h2>, ..., <h6>
        headers = soup.find_all(re.compile(r'^h[1-6]$'))
        # Retourner les textes contenus dans ces balises
        return [header.get_text() for header in headers]
    return []

# Exemple 
if __name__ == "__main__":
    file_path = "Jour3\example.html"  
    headers = find_headers(file_path)
    print("En-têtes trouvées :")
    for header in headers:
        print(header)

# partie2,6.py

from bs4 import BeautifulSoup

def create_bs_obj(file: str) -> BeautifulSoup:
    
    try:
        with open(file, 'r', encoding='utf-8') as html_file:
            content = html_file.read()
            soup = BeautifulSoup(content, 'html.parser')
            return soup
    except FileNotFoundError:
        print(f"Erreur : Le fichier {file} est introuvable.")
        return None

def extract_table(file: str) -> list[dict]:
    
    soup = create_bs_obj(file)
    if soup:
        table = soup.find('table')  
        rows = table.find_all('tr')  
        
        # Extraire les en-têtes du tableau
        headers = [header.get_text().strip().lower() for header in rows[0].find_all('th')]
        
        fruits = []
        # Parcourir les lignes de données (à partir de la deuxième ligne, donc on saute l'index 0)
        for row in rows[1:]:
            values = [cell.get_text().strip() for cell in row.find_all('td')]
            # Créer un dictionnaire pour chaque fruit
            fruit = dict(zip(headers, values))
            # Convertir le prix en float
            fruit['price'] = float(fruit['price'].replace('$', ''))
            fruits.append(fruit)
        
        return fruits
    return []

# Exemple 
if __name__ == "__main__":
    file_path = "Jour3\example.html"  
    fruits_info = extract_table(file_path)
    print("Informations sur les fruits extraites du tableau :")
    for fruit in fruits_info:
        print(fruit)
