# partie2.py

def format_with_fstring(username: str, age: int) -> str:
    """
    Prend un nom d'utilisateur et un âge, et retourne une chaîne formatée 
    en utilisant une f-string.

    :param username: Le nom d'utilisateur.
    :param age: L'âge de l'utilisateur.
    :return: Une chaîne du type "Hello {username}, you are {age} years old!"
    """
    return f"Hello {username}, you are {age} years old!"

# Exemple d'utilisation
if __name__ == "__main__":
    result = format_with_fstring("Alice", 30)
    print(result)  # Affiche: Hello Alice, you are 30 years old!
