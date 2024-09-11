def read_one_line(filename: str) -> str:
    with open(filename, 'r') as file:
        first_line = file.readline()
    return first_line

def write_text(filename: str, text: str):
    # Ouvre le fichier en mode écriture ('w'). Si le fichier n'existe pas, il sera créé.
    file = open(filename, 'w')
    # Écrit le texte dans le fichier.
    file.write(text)
    # Ferme le fichier
    file.close()

def copy_characters(input_file: str, output_file: str, nb: int):
    # Ouvre le fichier source en mode lecture ('r')
    with open(input_file, 'r') as source_file:
        characters = source_file.read(nb)
    
    # Ouvre le fichier de destination en mode ajout ('a')
    with open(output_file, 'a') as destination_file:
        destination_file.write('\n' + characters)
        
def read_all_lines(filename: str) -> (list[str], list[str]):
    # Ouvrir le fichier en mode lecture et lire toutes les lignes
    with open(filename, 'r') as file:
        lines = file.readlines()  # Toutes les lignes du fichier sous forme de liste
    
    # Créer une liste avec une ligne sur deux (en utilisant le slicing)
    lines_every_other = lines[::2]
    
    # Retourner le tuple contenant les deux listes
    return lines, lines_every_other

#exo5

def write_text_better(filename: str, text: str):
    with open(filename, "w") as file:
        file.write(text)

def copy_characters_better(input_file: str, output_file: str, nb: int):
    with open(input_file, "r") as infile, open(output_file, "a") as outfile:
        characters = infile.read(nb)
        outfile.write("\n" + characters)