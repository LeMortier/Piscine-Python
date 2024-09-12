def copy_characters(input_file: str, output_file: str, nb: int):
    # Ouvre le fichier source en mode lecture ('r')
    with open(input_file, 'r') as source_file:
        characters = source_file.read(nb)  # Lit nb caractères
    
    # Ouvre le fichier de destination en mode ajout ('a')
    with open(output_file, 'a') as destination_file:
        destination_file.write(characters)  # Écrit les caractères sans ajouter de saut de ligne supplémentaire
