from Creation import *
from ABR import *
from suppression import *
from exploration import *
from visualisation import *
from generateur import *
import matplotlib.pyplot as plt
import numpy as np
import customtkinter as ctk
import re

def is_number(string):
    return bool(re.match(r'^[0-9]+$', string))


def mainSuppr(val):
    

    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")

    root = ctk.CTk()
    root.geometry("500x200")
    root.title("Supprimer")

    frame = ctk.CTkFrame(master=root)
    frame.pack(pady=20, padx=60, fill="both", expand=True)
    if (recherche(arbre, val)):
        label = ctk.CTkLabel(
            master=frame, text=f"Le nombre {val} a bien été supprimé")
        frame1 = ctk.CTkFrame(master=frame,
                              width=50,
                              height=50,
                              corner_radius=50,
                              fg_color="green")
        delete_val(arbre, val)

    else:
        val = int(val)
        label = ctk.CTkLabel(master=frame, text=(f"Le nombre {val} n'existe pas"))
        frame1 = ctk.CTkFrame(master=frame,
                              width=50,
                              height=50,
                              corner_radius=50,
                              fg_color="red")
    label.pack(pady=12, padx=10)
    frame1.pack(pady=12, padx=10)
    root.mainloop()


def mainSupprimer():
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")

    root = ctk.CTk()
    root.geometry("500x200")
    root.title("Supprimer")

    frame = ctk.CTkFrame(master=root)
    frame.pack(pady=20, padx=60, fill="both", expand=True)
    entry = ctk.CTkEntry(
        master=frame, placeholder_text="Entrer la valeur a supprimer")
    entry.pack(pady=12, padx=10)
    btn4 = ctk.CTkButton(master=frame, text="Supprimer dans le csv",
                         command=lambda: mainDeleteCsv(entry.get()))
    btn4.pack(pady=12, padx=10)
    btn5 = ctk.CTkButton(master=frame, text="Supprimer a la volée",
                         command=lambda: mainSupprimerObj(entry.get()))
    btn5.pack(pady=12, padx=10)
    root.mainloop()


def mainRechercheViz(arbre, val):
    
    val = int(val)
    if (recherche(arbre, val)):
        visualize_with_red_one(arbre, val)
    else:
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        root = ctk.CTk()
        root.geometry("500x100")
        root.title("Error")

        frame = ctk.CTkFrame(master=root)
        frame.pack(pady=20, padx=60, fill="both", expand=True)
        label = ctk.CTkLabel(
            master=frame, text="erreur : le nombre n'est pas dans l'arbre")
        label.pack(pady=12, padx=10)
        root.mainloop()


def mainRecherche(arbre, val):
    
    print(recherche(arbre, val))
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")

    root = ctk.CTk()
    root.geometry("500x200")
    root.title("Rechercher")

    frame = ctk.CTkFrame(master=root)
    frame.pack(pady=20, padx=60, fill="both", expand=True)
    if (is_number(str(val)) == False):
        label = ctk.CTkLabel(master=frame, text="Erreur : le nombre n'est pas un entier")
        frame1 = ctk.CTkFrame(master=frame,
                              width=50,
                              height=50,
                              corner_radius=50,
                              fg_color="purple")
    else:
        val = int(val)
        if (recherche(arbre, val)):
            label = ctk.CTkLabel(master=frame, text=f"Le nombre {val} est dans l'arbre")
            frame1 = ctk.CTkFrame(master=frame,
                                width=50,
                                height=50,
                                corner_radius=50,
                                fg_color="green")

        else:
            label = ctk.CTkLabel(
                master=frame, text=f"Le nombre {val} n'est pas dans l'arbre")
            frame1 = ctk.CTkFrame(master=frame,
                                width=50,
                                height=50,
                                corner_radius=50,
                                fg_color="red")
    label.pack(pady=12, padx=10)
    frame1.pack(pady=12, padx=10)
    root.mainloop()


def mainVisualisation():
    visualize(arbre)


def mainSupprimerObj(val):
    
    
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")

    root = ctk.CTk()
    root.geometry("500x200")
    root.title("Rechercher")

    frame = ctk.CTkFrame(master=root)
    frame.pack(pady=20, padx=60, fill="both", expand=True)
    if (is_number(str(val)) == False):
        label = ctk.CTkLabel(master=frame, text="Erreur : le nombre n'est pas un entier")
        frame1 = ctk.CTkFrame(master=frame,
                              width=50,
                              height=50,
                              corner_radius=50,
                              fg_color="purple")
    else:
        val = int(val)
        if (recherche(arbre, val)):
            delete_val(arbre, val)
            label = ctk.CTkLabel(master=frame, text=f"Le nombre {val} a bien été supprimé")
            frame1 = ctk.CTkFrame(master=frame,
                                width=50,
                                height=50,
                                corner_radius=50,
                                fg_color="green")

        else:
            label = ctk.CTkLabel(
                master=frame, text=f"Le nombre {val} n'existe pas, il n'a pas été supprimé")
            frame1 = ctk.CTkFrame(master=frame,
                                width=50,
                                height=50,
                                corner_radius=50,
                                fg_color="red")
    label.pack(pady=12, padx=10)
    frame1.pack(pady=12, padx=10)
    root.mainloop()


def mainInsererObj(val):
    
    
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")

    root = ctk.CTk()
    root.geometry("500x200")
    root.title("Rechercher")

    frame = ctk.CTkFrame(master=root)
    frame.pack(pady=20, padx=60, fill="both", expand=True)
    arbre.insert(val)
    if (is_number(str(val)) == False):
        label = ctk.CTkLabel(master=frame, text="Erreur : le nombre n'est pas un entier")
        frame1 = ctk.CTkFrame(master=frame,
                              width=50,
                              height=50,
                              corner_radius=50,
                              fg_color="purple")
    else:
        val = int(val)
        label = ctk.CTkLabel(master=frame, text=f"Le nombre {val} a bien été inseré")
        frame1 = ctk.CTkFrame(master=frame,
                              width=50,
                              height=50,
                              corner_radius=50,
                              fg_color="green")

    label.pack(pady=12, padx=10)
    frame1.pack(pady=12, padx=10)
    root.mainloop()


def mainInsererCsv(val):
    val = int(val)
    
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")

    root = ctk.CTk()
    root.geometry("500x200")
    root.title("Rechercher")

    frame = ctk.CTkFrame(master=root)
    frame.pack(pady=20, padx=60, fill="both", expand=True)
    csvadd(val)
    arbre.insert(val)
    print(val, is_number(str(val)))
    if (is_number(str(val)) == False):
        label = ctk.CTkLabel(master=frame, text="Erreur : le nombre n'est pas un entier")
        frame1 = ctk.CTkFrame(master=frame,
                              width=50,
                              height=50,
                              corner_radius=50,
                              fg_color="purple")
    if (is_number(str(val)) == True):
        val = int(val)
        label = ctk.CTkLabel(master=frame, text=f"Le nombre {val} a bien été inseré")
        frame1 = ctk.CTkFrame(master=frame,
                              width=50,
                              height=50,
                              corner_radius=50,
                              fg_color="green")

    label.pack(pady=12, padx=10)
    frame1.pack(pady=12, padx=10)
    root.mainloop()
    


def mainDeleteCsv(val):
    
    
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")

    root = ctk.CTk()
    root.geometry("500x200")
    root.title("Supprimer")

    frame = ctk.CTkFrame(master=root)
    frame.pack(pady=20, padx=60, fill="both", expand=True)
    if (is_number(str(val)) == False):
        label = ctk.CTkLabel(master=frame, text="Erreur : le nombre n'est pas un entier")
        frame1 = ctk.CTkFrame(master=frame,
                              width=50,
                              height=50,
                              corner_radius=50,
                              fg_color="red")
    else:
        val = int(val)
        if (recherche(arbre, val)):
            csvdel(val)
            delete_val(arbre, val)
            label = ctk.CTkLabel(master=frame, text=(f"Le nombre {val} a bien été supprimé"))
            frame1 = ctk.CTkFrame(master=frame,
                                  width=50,
                                  height=50,
                                  corner_radius=50,
                                  fg_color="green")

        else:
            label = ctk.CTkLabel(
                master=frame, text=f"Le nombre {val} n'existe pas, il n'a pas été supprimé")
            frame1 = ctk.CTkFrame(master=frame,
                                  width=50,
                                  height=50,
                                  corner_radius=50,
                                  fg_color="red")
        label.pack(pady=12, padx=10)
        frame1.pack(pady=12, padx=10)
        root.mainloop()

    


def mainInsert():
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")

    root = ctk.CTk()
    root.geometry("500x200")
    root.title("Inserer")

    frame = ctk.CTkFrame(master=root)
    frame.pack(pady=20, padx=60, fill="both", expand=True)
    entry = ctk.CTkEntry(
        master=frame, placeholder_text="Entrer la valeur a inserer")
    entry.pack(pady=12, padx=10)
    btn4 = ctk.CTkButton(master=frame, text="Inserer dans le csv",
                         command=lambda: mainInsererCsv(entry.get()))
    btn4.pack(pady=12, padx=10)
    btn5 = ctk.CTkButton(master=frame, text="Inserer a la volée",
                         command=lambda: mainInsererObj(entry.get()))
    btn5.pack(pady=12, padx=10)
    root.mainloop()


def mainListe():
    print(csvread())
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")

    root = ctk.CTk()
    root.geometry("500x200")
    root.title("Liste")

    frame = ctk.CTkFrame(master=root)
    frame.pack(pady=20, padx=60, fill="both", expand=True)
    label = ctk.CTkLabel(master=frame, text=csvread(), wraplength=350)
    label.pack(pady=12, padx=10)
    root.mainloop()


def visualisationTri():
    visualize_with_animation_parcours(arbre)


def mainTrier():
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")

    root = ctk.CTk()
    root.geometry("500x300")
    root.title("Trier")

    frame = ctk.CTkFrame(master=root)
    frame.pack(pady=20, padx=60, fill="both", expand=True)
    label = ctk.CTkLabel(
        master=frame, text=parcours_infixe_liste_itératif(arbre), wraplength=350)
    label.pack(pady=12, padx=10)
    btn5 = ctk.CTkButton(master=frame, text="visualiser",
                         command=visualisationTri)
    btn5.place(x=120, y=200)
    root.mainloop()


def mainRechercher():
    print(parcours_infixe_liste_itératif(arbre))
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")

    root = ctk.CTk()
    root.geometry("500x200")
    root.title("Rechercher")

    frame = ctk.CTkFrame(master=root)
    frame.pack(pady=20, padx=60, fill="both", expand=True)
    entry = ctk.CTkEntry(
        master=frame, placeholder_text="Entrez la valeur a rechercher")
    entry.pack(pady=12, padx=10)
    btn4 = ctk.CTkButton(master=frame, text="rechercher",
                         command=lambda: mainRecherche(arbre, entry.get()))
    btn4.pack(pady=12, padx=10)
    root.mainloop()

listefini = []
def tab_équilibrer(liste):
    if len(liste)==1:
        return liste
    left=liste[0:len(liste)//2]
    tab_équilibrer(left)
    right=liste[len(liste)//2:len(liste)]
    tab_équilibrer(right)
    listefini.append(liste[len(liste)//2])
    return listefini

def mainEquilibre(arbre):
    reverse = []
    reverse = list(reversed(tab_équilibrer(parcours_infixe_liste_itératif(arbre))))
    print(reverse)
    csvwrite(reverse)

def app():
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")

    root = ctk.CTk()
    root.geometry("600x500")
    root.title("Arbre Binaire de Recherche")

    frame = ctk.CTkFrame(master=root)
    frame.pack(pady=20, padx=60, fill="both", expand=True)

    label = ctk.CTkLabel(
        master=frame, text="Bienvenue dans l'application de visualisation d'arbre binaire de recherche")
    label.pack(pady=12, padx=10)

    btn = ctk.CTkButton(master=frame, text="Voir la liste", command=mainListe)
    btn.place(x=100, y=50)

    btn2 = ctk.CTkButton(
        master=frame, text="Trier la liste grace a l'arbre", command=mainTrier)
    btn2.place(x=250, y=50)

    btn1 = ctk.CTkButton(
        master=frame, text="Visualiser l'arbre", command=mainVisualisation)
    btn1.place(x=175, y=100)

    btn4 = ctk.CTkButton(master=frame, text="Supprimer", command=mainSupprimer)
    btn4.place(x=175, y=150)

    btn3 = ctk.CTkButton(master=frame, text="Rechercher",
                         command=mainRechercher)
    btn3.place(x=175, y=200)

    btn4 = ctk.CTkButton(master=frame, text="Inserer", command=mainInsert)
    btn4.place(x=175, y=250)

    btn4 = ctk.CTkButton(master=frame, text="Equilibrer", command=lambda: mainEquilibre(arbre))
    btn4.place(x=175, y=300)

    label4 = ctk.CTkLabel(
        master=frame, text="nombre de noeuds : "+str(len(parcours_infixe_liste_itératif(arbre))))
    label4.place(x=175, y=340)
    label4 = ctk.CTkLabel(
        master=frame, text="hauteur de l'arbre : "+str(hauteur(arbre)))
    label4.place(x=175, y=375)

    root.mainloop()


    
if __name__ == "__main__":
    csvwrite(generateur(25))
    arbre = create()
    
    #visualize(arbre)
    app()
