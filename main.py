from Creation import create
from ABR import *
from exploration import *
from visualisation import visualize
import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":
    arbre = create()
    parcours_infixe(arbre)
    visualize(arbre)
    print(parcours_infixe(arbre))
    print(arbre.left.val)



    



