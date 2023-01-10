import csv
from ABR import *


liste = []

# Ouverture du fichier csv
with open('ABRcsv.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    # Lecture des nombres
    for row in csv_reader:
        for number in row:
            liste.append(number)

for element in liste:
    arbre.insert(element)
