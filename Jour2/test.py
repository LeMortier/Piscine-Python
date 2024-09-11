def read_all_lines(filename: str) -> (list[str], list[str]):
    # Ouvrir le fichier en mode lecture et lire toutes les lignes
    with open(filename, 'r') as file:
        lines = file.readlines()  # Toutes les lignes du fichier sous forme de liste
    
    # Créer une liste avec une ligne sur deux (en utilisant le slicing)
    lines_every_other = lines[::2]
    
    # Retourner le tuple contenant les deux listes
    return lines, lines_every_other
