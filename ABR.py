
class ABR:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def insert(self, val):
        if self.val:
            if val < self.val:
                if self.left is None:
                    self.left = ABR(val)
                else:
                    self.left.insert(val)
            elif val > self.val:
                if self.right is None:
                    self.right = ABR(val)
                else:
                    self.right.insert(val)
        else:
            self.val = val

    def est_feuille(self):
        if self.left == None and self.right == None:
            return True
        else:
            return False

    def est_pere(self):
        if self.left != None or self.right != None:
            return True
        else:
            return False
    
    def est_racine(self):
        if self.left == None and self.right == None:
            return True
        else:
            return False


    
    
    

# arbre = ABR(12)
# arbre.insert(6)
# arbre.insert(14)
# arbre.insert(3)
