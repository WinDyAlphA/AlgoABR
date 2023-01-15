from Creation import create
from ABR import *
from suppression import *
from exploration import *
from visualisation import visualize
import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":
    arbre = create()
    delete_val(arbre, 17)
    parcours_infixe(arbre)
    visualize(arbre)
    print(arbre.val)
    print(arbre.left.val)
    
    
    



