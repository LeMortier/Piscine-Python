# Exercice 1

def concat_with_space(a: str, b: str) -> str:
    sentence = a+ ' ' +b
    print(sentence)
    return(sentence)

#concat_with_space('Hello', 'World!')

# Exercice 2

def format_with_fstring(username: str, age: int) -> str:
    a = username
    b = age
    sentence = f"Hello {a}" + f", you are {b} years old!"
    print(sentence)
    return(sentence)

#format_with_fstring('Ad', 19)
