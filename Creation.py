import csv
from ABR import * 

arbre = ABR(12)
arbre.insert(6)
arbre.insert(14)
arbre.insert(3)

print(arbre.left.val)
print(arbre.right.val)



    # Ouverture du fichier csv
with open('nom_fichier.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    # Lecture des nombres
    for row in csv_reader:
        for number in row:
            print(number)
