# %% [markdown]
# # Introduction aux types de cellules dans un Notebook Jupyter
# 
# Ce notebook démontre l'utilisation des cellules de code, de markdown et des cellules brutes dans Jupyter. Nous allons également effectuer quelques opérations simples sur une liste de valeurs numériques.
# 

# %%
print("Hello World!")


# %%
my_list = [10, 20, 30, 40, 50, 60]
my_list


# %% [markdown]
# Dans la cellule suivante, nous allons calculer plusieurs statistiques sur `my_list` : la somme, la moyenne, la valeur maximale et la valeur minimale. Ces valeurs seront affichées sous forme de tuple.
# 

# %%
total = sum(my_list)
average = round(total / len(my_list), 2)
maximum = max(my_list)
minimum = min(my_list)

(total, average, maximum, minimum)


# %%
import pandas as pd


# %%
# Utilisation de %time pour mesurer le temps de chargement d'un fichier CSV
%time df = pd.read_csv('sales.csv')


# %%
# Utilisation de %%timeit pour évaluer la performance d'une manipulation répétée
%timeit -n 25 -r 20
df.describe()  # Obtenir des statistiques descriptives sur les données


# %%
# Affiche toutes les variables définies dans l'environnement
%whos


# %%
# Liste toutes les commandes magiques disponibles
%lsmagic



