from Creation import *

class ABR:
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None
        self.height = 0

    def insert(self, val):
        if self.val:
            if val <= self.val:
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

        """self.height = 1 + max(self.get_height(self.left), self.get_height(self.right))

        balance = self.get_balance()

        # Left Left Case
        if balance > 1 and val < self.left.val:
            return self.right_rotate()

        # Right Right Case
        if balance < -1 and val > self.right.val:
            return self.left_rotate()

        # Left Right Case
        if balance > 1 and val > self.left.val:
            self.left = self.left.left_rotate()
            return self.right_rotate()

        # Right Left Case
        if balance < -1 and val < self.right.val:
            self.right = self.right.right_rotate()
            return self

    def right_rotate(self):
        new_root = self.left
        self.left = new_root.right
        new_root.right = self

        self.height = 1 + max(self.get_height(self.left), self.get_height(self.right))
        new_root.height = 1 + max(self.get_height(new_root.left), self.get_height(new_root.right))

        return new_root

    def left_rotate(self):
        new_root = self.right
        self.right = new_root.left
        new_root.left = self

        self.height = 1 + max(self.get_height(self.left), self.get_height(self.right))
        new_root.height = 1 + max(self.get_height(new_root.left), self.get_height(new_root.right))

        return new_root

    def get_height(self, root):
        if not root:
            return -1
        return root.height

    def get_balance(self):
        return self.get_height(self.left) - self.get_height(self.right)"""

    def est_feuille(self):
        if self.left == None and self.right == None:
            return True
        else:
            return False

    def nb_feuilles(self):
        if self.est_feuille():
            return 1
        else:
            return self.left.nb_feuilles() + self.right.nb_feuilles()

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
