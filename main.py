from Creation import *
from ABR import *
from suppression import *
from exploration import *
from visualisation import *
import matplotlib.pyplot as plt
import numpy as np
import customtkinter as ctk

def mainRechercheViz(arbre,val):
    val = int(val)
    if (recherche(arbre,val)):
        visualize_with_red_one(arbre,val)
    else:
        ctk.set_appearance_mode("dark") 
        ctk.set_default_color_theme("dark-blue")

        root = ctk.CTk()
        root.geometry("500x100")
        root.title("Error")

        frame = ctk.CTkFrame(master=root)
        frame.pack(pady=20, padx=60, fill="both", expand=True)
        label = ctk.CTkLabel(master=frame, text="erreur : le nombre n'est pas dans l'arbre")
        label.pack(pady=12, padx=10)
        root.mainloop()

def mainRecherche(arbre,val):
    val = int(val)
    print(recherche(arbre,val))
    ctk.set_appearance_mode("dark") 
    ctk.set_default_color_theme("dark-blue")

    root = ctk.CTk()
    root.geometry("500x200")
    root.title("Rechercher")

    frame = ctk.CTkFrame(master=root)
    frame.pack(pady=20, padx=60, fill="both", expand=True)
    if (recherche(arbre,val)):
        label = ctk.CTkLabel(master=frame, text="Le nombre est dans l'arbre")
        frame1 = ctk.CTkFrame(master=frame,
                               width=50,
                               height=50,
                               corner_radius=10,
                               fg_color="green")
        
    else:
        label = ctk.CTkLabel(master=frame, text="Le nombre n'est pas dans l'arbre")
        frame1 = ctk.CTkFrame(master=frame,
                               width=50,
                               height=50,
                               corner_radius=10,
                               fg_color="red")
    label.pack(pady=12, padx=10)
    frame1.pack(pady=12, padx=10)
    root.mainloop()


def mainVisualisation():
    visualize(arbre)

def mainListe():
    print(csvread())
    ctk.set_appearance_mode("dark") 
    ctk.set_default_color_theme("dark-blue")

    root = ctk.CTk()
    root.geometry("500x100")
    root.title("Liste")

    frame = ctk.CTkFrame(master=root)
    frame.pack(pady=20, padx=60, fill="both", expand=True)
    label = ctk.CTkLabel(master=frame, text=csvread())
    label.pack(pady=12, padx=10)
    root.mainloop()

def triFixe():
    print(parcours_infixe_liste_itératif(arbre))
    ctk.set_appearance_mode("dark") 
    ctk.set_default_color_theme("dark-blue")

    root = ctk.CTk()
    root.geometry("500x100")
    root.title("Trier")

    frame = ctk.CTkFrame(master=root)
    frame.pack(pady=20, padx=60, fill="both", expand=True)
    label = ctk.CTkLabel(master=frame, text=parcours_infixe_liste_itératif(arbre))
    label.pack(pady=12, padx=10)
    root.mainloop()

def visualisationTri():
    visualize_with_animation_parcours(arbre)

def mainTrier():
    ctk.set_appearance_mode("dark") 
    ctk.set_default_color_theme("dark-blue")

    root = ctk.CTk()
    root.geometry("500x200")
    root.title("Trier")

    frame = ctk.CTkFrame(master=root)
    frame.pack(pady=20, padx=60, fill="both", expand=True)
    btn4 = ctk.CTkButton(master=frame, text="afficher la liste", command=triFixe)
    btn4.pack(pady=12, padx=10)
    btn5 = ctk.CTkButton(master=frame, text="visualiser", command=visualisationTri)
    btn5.pack(pady=12, padx=10)
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
    entry = ctk.CTkEntry(master=frame, placeholder_text="Entrer la valeur a rechercher")
    entry.pack(pady=12, padx=10)
    btn4 = ctk.CTkButton(master=frame, text="rechercher", command=lambda:mainRecherche(arbre,entry.get()))
    btn4.pack(pady=12, padx=10)
    btn5 = ctk.CTkButton(master=frame, text="visualiser", command=lambda:mainRechercheViz(arbre,entry.get()))
    btn5.pack(pady=12, padx=10)
    root.mainloop()
    

def app():
    ctk.set_appearance_mode("dark") 
    ctk.set_default_color_theme("dark-blue")

    root = ctk.CTk()
    root.geometry("600x350")
    root.title("Arbre Binaire de Recherche")

    frame = ctk.CTkFrame(master=root)
    frame.pack(pady=20, padx=60, fill="both", expand=True)

    label = ctk.CTkLabel(master=frame, text="Bienvenue dans l'application de visualisation d'arbre binaire de recherche")
    label.pack(pady=12, padx=10)

    btn = ctk.CTkButton(master=frame, text="voir la liste", command=mainListe)
    btn.place(x=100, y=50)

    btn2 = ctk.CTkButton(master=frame, text="trier la liste grace a l'arbre", command=mainTrier)
    btn2.place(x=250, y=50)

    btn1 = ctk.CTkButton(master=frame, text="visualiser l'arbre", command=mainVisualisation)
    btn1.place(x=175, y=100)

    btn3 = ctk.CTkButton(master=frame, text="rechercher", command=mainRechercher)
    btn3.place(x=175, y=150)



    root.mainloop()
    



if __name__ == "__main__":
    arbre = create()
    delete_val(arbre, 17)
    parcours_infixe(arbre)
    # visualize(arbre)
    print(parcours_infixe(arbre))
    print(arbre.left.val)
    app()








    
    
    



