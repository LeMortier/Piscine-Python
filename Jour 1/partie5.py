# Exercice 1

import sys

def list_discovery() -> list:
    numbers = list(map(int, sys.argv[1:6]))
    numbers.sort(reverse=True)
    numbers.pop()
    print(f"Numbers has {len(numbers)} elements and the sum of them all is {sum(numbers)}.")
    numbers.append(int(sys.argv[6]))
    return numbers

#list_discovery()
#python partie5.py 10 20 30 40 50 60

# Exercice 2

def dict_creation() -> dict:
    args = sys.argv[1:]
    my_dict = dict(zip(args[::2], args[1::2]))
    return my_dict

def dict_display(my_dict: dict):
    print("\nClés :")
    print("\n".join(my_dict.keys()))
    print("\nValeurs :")
    print("\n".join(my_dict.values()))
    print("\nPaires clé-valeur :")
    for key, value in my_dict.items():
        print(f"Key: {key} - Value: {value}")
        
my_dict = dict_creation()
dict_display(my_dict)

#python partie5.py key1 value1 key2 value2 key3 value3

# Exercice 3

def tuple_discovery(a, b, c, d) -> tuple:
    return (d, c, b, a)

def tuple_display(tpl: tuple):
    for item in tpl:
        print(item)
        
my_tuple = tuple_discovery(1, 2, 3, 4)
tuple_display(my_tuple)

# Exercice 4

def set_discovery(l1: list, l2: list) -> tuple:
    set1 = set(l1)
    set2 = set(l2)
    union_result = set1.union(set2)
    intersection_result = set1.intersection(set2)
    difference_result = set1.difference(set2)
    symmetric_difference_result = set1.symmetric_difference(set2)
    return (union_result, intersection_result, difference_result, symmetric_difference_result)

list1 = [1, 2, 3, 4, 4]
list2 = [3, 4, 5, 6]

result = set_discovery(list1, list2)
#print(result)

# Exercice 5

def power_via_comprehension(numbers: list[int]) -> list[int]:
    return [x**2 if x < 0 else -x for x in numbers]

#power_via_comprehension([-1, 2, -3, 4, -5])
