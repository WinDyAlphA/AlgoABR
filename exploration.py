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

def Tri_bulle(tab):
    for i in range(len(tab)):
        for j in range(len(tab)-1):
            if tab[j]>tab[j+1]:
                tab[j],tab[j+1]=tab[j+1],tab[j]
    return tab
        
def Supprimer(ABR,val):
    if ABR.recherche(val):
        ABR.val=ABR.Tri_bulle(ABR)[1]
        ABR.Tri_bulle(ABR).pop(0)
        return ABR
    else:
        return False