def format_with_fstring(username: str, age: int) -> str:
    """Format une chaîne de caractères personnalisée avec un nom d'utilisateur et un âge.
        username: Le nom d'utilisateur.
        age: L'âge de l'utilisateur.

    Retourne:
        La chaîne formatée.
    """

    return f"Hello {username}, you are {age} years old!"

# Exemple 
result = format_with_fstring("Tonio", 22)
print(result)  