# Exercice 1

def multiply(a: int, b: int):
    multi = a*b
    print(multi)
    return multi

#multiply(2, 4)

# Exercice 2

def compare(a: int, b: int):
    if a == b:
        print(f"Les deux nombres et sont égaux")
    elif a <= b:
        print(f"Le premier nombre est plus petit que le second")
    elif a >= b:
        print(f"Le premier nombre est plus grand que le second")

#compare(5, 5)

# Exercice 3

def counting(x:int):
    result = ", ".join(str(i) for i in range(1, x+1, 2))
    print(result)
    return(result)

#counting(10)

# Exercice 4

def ask_user():
    while (ask := input("Entrez un mot (ou 'exit' pour quitter) : ")) != "exit":
        print(f"Vous avez entré : {ask}")
        return(f"Vous avez entré : {ask}")

#ask_user()

# Exercice 5

def safe_divide(a :int, b:int):
    try:
        operation = a / b
        print(operation)
        return operation
    except ZeroDivisionError:
        print("Impossible de diviser par zéro")
        return None

#safe_divide(5, 2)

# Exercice 6

def display_square(size: int, char: str):
    for i in range(size):
        for j in range(size):
            print(char, end='')
        print()

#display_square(5, '#')
