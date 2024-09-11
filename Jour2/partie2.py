import csv

def native_csv_read(file: str) -> list[tuple]:
    result = []
    
    # Ouvre le fichier en mode lecture
    with open(file, 'r') as csv_file:
        # Crée un itérateur pour lire le fichier ligne par ligne
        lines = iter(csv_file)
        
        next(lines)
        
        # Lire les lignes restantes
        for index, line in enumerate(lines):
            # Supprime les espaces superflus en début et fin de ligne et découpe en utilisant ';' 
            values = line.strip().split(';')
            
            result.append((index, *values))
    
    return result

def native_csv_write(file: str, headers: list, data: list[tuple]):
    # Ouvre le fichier en mode écriture
    with open(file, 'w') as csv_file:
        
        csv_file.write(','.join(headers) + '\n')
         
        for row in data:
            # Convertit chaque élément du tuple (sauf l'index) en chaîne de caractères
            csv_file.write(','.join(map(str, row[1:])) + '\n')
            
