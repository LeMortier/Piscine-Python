def concat_with_space(a: str, b: str) -> str:
    """
    Prend deux chaînes, les concatène avec un espace entre elles, 
    et retourne le résultat.

    :param a: Première chaîne.
    :param b: Deuxième chaîne.
    :return: Chaîne concaténée avec un espace entre `a` et `b`.
    """
    return a + " " + b

# Exemple 
if __name__ == "__main__":
    result = concat_with_space("Bonjour", "le monde")
    print(result)  # Affiche: Bonjour le monde

def format_with_fstring(username: str, age: int) -> str:
    """Format une chaîne de caractères personnalisée avec un nom d'utilisateur et un âge.
    
        username: Le nom d'utilisateur.
        age: L'âge de l'utilisateur.

    Retourne :
        La chaîne formatée.
    """

    return f"Hello {username}, you are {age} years old!"

# Exemple d'utilisation :
result = format_with_fstring("Bob", 4)
print(result)  # result is name and age 