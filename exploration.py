def recherche(ABR, val):
        if (val in parcours_infixe_liste_itératif(ABR)):
            return True
        else:
            return False


def hauteur(ABR):
    if ABR is None:
        return -1
    return 1 + max(hauteur(ABR.left), hauteur(ABR.right))
    
def parcours_infixe(ABR):
    if ABR is not None:
        parcours_infixe(ABR.left)
        print(ABR.val)
        parcours_infixe(ABR.right)

def parcours_infixe_liste_itératif(ABR):
    liste = []
    pile = []
    while ABR is not None or len(pile) != 0:
        while ABR is not None:
            pile.append(ABR)
            ABR = ABR.left
        ABR = pile.pop()
        liste.append(ABR.val)
        ABR = ABR.right
    return liste
    

