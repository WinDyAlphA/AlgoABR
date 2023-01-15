from Creation import create
from ABR import *
from visualisation import visualize
import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":
    arbre = create()
    visualize(arbre)
    print(arbre.val)
    print(arbre.left.val)
    print(arbre.right.val)
    