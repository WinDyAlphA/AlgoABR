from Creation import *
from ABR import *
from exploration import *
from visualisation import visualize
import matplotlib.pyplot as plt
import numpy as np
import customtkinter as ctk

def mainRecherche(arbre,val):
    val = int(val)
    print(recherche(arbre,val))
    ctk.set_appearance_mode("dark") 
    ctk.set_default_color_theme("dark-blue")

    root = ctk.CTk()
    root.geometry("500x200")
    root.title("Liste")

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

def mainTrier():
    print(parcours_infixe_liste_itératif(arbre))
    ctk.set_appearance_mode("dark") 
    ctk.set_default_color_theme("dark-blue")

    root = ctk.CTk()
    root.geometry("500x100")
    root.title("Liste")

    frame = ctk.CTkFrame(master=root)
    frame.pack(pady=20, padx=60, fill="both", expand=True)
    label = ctk.CTkLabel(master=frame, text=parcours_infixe_liste_itératif(arbre))
    label.pack(pady=12, padx=10)
    root.mainloop()
    
def mainRechercher():
    print(parcours_infixe_liste_itératif(arbre))
    ctk.set_appearance_mode("dark") 
    ctk.set_default_color_theme("dark-blue")

    root = ctk.CTk()
    root.geometry("500x200")
    root.title("Liste")

    frame = ctk.CTkFrame(master=root)
    frame.pack(pady=20, padx=60, fill="both", expand=True)
    entry = ctk.CTkEntry(master=frame, placeholder_text="Entrer la valeur a rechercher")
    entry.pack(pady=12, padx=10)
    btn4 = ctk.CTkButton(master=frame, text="rechercher", command=lambda:mainRecherche(arbre,entry.get()))
    btn4.pack(pady=12, padx=10)
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
    btn.pack(pady=12, padx=10)

    btn2 = ctk.CTkButton(master=frame, text="trier la liste grace a l'arbre", command=mainTrier)
    btn2.pack(pady=12, padx=10)

    btn1 = ctk.CTkButton(master=frame, text="visualiser l'arbre", command=mainVisualisation)
    btn1.pack(pady=12, padx=10)

    btn3 = ctk.CTkButton(master=frame, text="rechercher", command=mainRechercher)
    btn3.pack(pady=12, padx=10)



    root.mainloop()
    



if __name__ == "__main__":
    arbre = create()
    parcours_infixe(arbre)
    # visualize(arbre)
    print(parcours_infixe(arbre))
    print(arbre.left.val)
    app()








    



