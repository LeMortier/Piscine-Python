def multiply(a: int, b: int) -> int:
    return a * b
if __name__ == "__main__":
   
    nb1 = 7
    nb2 = 6
    # Appel de la fonction multiply
    resultat = multiply(nb1, nb2)
    # Affichage du résultat dans la console
    print(f"Le produit de {nb1} multiplié par {nb2} est : {resultat}")
    
def compare(a: int, b: int):
    if a > b:
        print("premier nombre plus grand que le second")
    elif a < b:
        print("premier nombre plus petit que le second")
    else:
        print("premier nombreégal au second")

# exemples 
compare(5, 7)
compare(18, 33)
compare(72, 56)

def counting(x: int):
    # génere une liste de nombres impairs de 1 à x
    # range(start, stop, step) : start est inclus, stop est exclus
    # les nombres impairs, start = 1 et step = 2
    # s'arrête à x + 1 pour inclure x si x est impair
    for num in range(1, x + 1, 2):
        if num != 1:
            print(", ", end="")
        print(num, end="")
    print()  # ajoute une nouvelle ligne après la liste des nombres

# exemples 
counting(109)  
counting(5)   
counting(1) 

def ask_user():
  """Demande à l'utilisateur de saisir des mots jusqu'à ce qu'il entre 'exit'."""

  while (mot := input("Entrez un mot (ou 'exit' pour quitter) : ")) != 'exit':
    print(f"Vous avez entré : {mot}")

# Appel de la fonction
ask_user()

def safe_divide(a: int, b: int) -> float | None:
    try:
        # Tente de diviser a par b
        result = a / b
    except ZeroDivisionError:
        # Gère l'exception de division par zéro
        print("Impossible à diviser par zéro")
        return None
    return result

# exemples
print(safe_divide(10, 2))  # Affiche le résultat voulu
print(safe_divide(10, 0))  # Affiche impossible à diviser par zéro et retourne ==> None

def display_square(size: int, char: str):
  """Affiche un carré de taille 'size' rempli du caractère 'char'.
    size: La longueur d'un côté du carré.
    char: Le caractère à utiliser pour remplir le carré.
  """
  for _ in range(size):
    for _ in range(size):
      print(char, end="")
    print()

# exemple
display_square(7, '.')





