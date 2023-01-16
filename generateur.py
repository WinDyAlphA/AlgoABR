import random
import csv


def generateur(n):
    liste = []
    for i in range(n):
        liste.append(random.randint(0, 100))
    return liste


def csvwrite(liste):
    with open('ABRcsv.csv', 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(liste)


def csvadd(val):
    val = str(val)
    with open('ABRcsv.csv', 'a', newline='') as csv_file:
        csv_file.write(f",{val}")

def csvdel(val):
    val = str(val)
    with open("ABRcsv.csv", "r") as file:
        reader = csv.reader(file)
        lines = []
        found = False
        for line in reader:
            new_line = []
            for x in line:
                if x == val and not found:
                    found = True
                    continue
                new_line.append(x)
            lines.append(new_line)

    with open("ABRcsv.csv", "w") as file:
        writer = csv.writer(file)
        writer.writerows(lines)
