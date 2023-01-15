def recherche(self, val):
        if self.val:
            if val < self.val:
                if self.left is None:
                    return False
                else:
                    return self.left.recherche(val)
            elif val > self.val:
                if self.right is None:
                    return False
                else:
                    return self.right.recherche(val)
            else:
                return True
        else:
            return False
def recherchehauteur(self,val):
    if self.val:
        if val < self.val:
            if self.left is None:
                return False
            else:
                  return self.left.recherchehauteur(val)+1
        elif val > self.val:
            if self.right is None:
                return False
            else:
                return self.right.recherchehauteur(val)+1
        else:
            return 0
    else:
        return False

def parcours_infixe(ABR):
    if ABR is not None:
        parcours_infixe(ABR.left)
        print(ABR.val)
        parcours_infixe(ABR.right)

def parcours_infixe_liste(ABR):
    liste = []
    if ABR is not None:
        parcours_infixe_liste(ABR.left)
        liste.append(ABR.val)
        parcours_infixe_liste(ABR.right)
    return liste
