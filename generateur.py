import random
import csv

def generateur(n):
    liste = []
    for i in range(n):
        liste.append(random.randint(0,100))
    return liste

def csvwrite(liste):
    with open('ABRcsv.csv', 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(liste)
    