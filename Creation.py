import csv
from ABR import *

# arbre = ABR(12)
# arbre.insert(6)
# arbre.insert(14)
# arbre.insert(3)

# print(arbre.left.val)
# print(arbre.right.val)
def csvread():
    liste = []
    with open('ABRcsv.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        # Lecture des nombres
        for row in csv_reader:
            for number in row:
                try:
                    liste.append(int(number))
                except ValueError:
                    print("Erreur : '{}' n'est pas un nombre valide.".format(number))
                    return
    return liste

    
def create():
    liste = []

# Ouverture du fichier csv
    liste =csvread()


    for idx, element in enumerate(liste):
        if idx == 0:
            arbre = ABR(int(element))
        else:
            arbre.insert(int(element))
    return arbre