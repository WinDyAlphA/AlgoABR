
from ABR import *
import matplotlib.pyplot as plt

def visualize(self):
        def dfs(node, x, y, spacing):
            if node:
                plt.scatter(x, y, s=1000, facecolors='none', edgecolors='b')
                plt.text(x, y, str(node.val), ha='center', va='center', fontsize=15)
                if node.left:
                    plt.plot([x-spacing, x], [y-1, y], color='gray', linewidth=1.5)
                    dfs(node.left, x-spacing, y-1, spacing/2)
                if node.right:
                    plt.plot([x+spacing, x], [y-1, y], color='gray', linewidth=1.5)
                    dfs(node.right, x+spacing, y-1, spacing/2)

        plt.figure(figsize=(8, 6))
        plt.axis('off')
        dfs(self, 0, 0, 1)
        plt.show()

def visualize_with_red_one(self,val):
        def dfs(node, x, y, spacing):
            if node:
                if node.val == val:
                    plt.scatter(x, y, s=1000, facecolors='none', edgecolors='r')
                else:
                    plt.scatter(x, y, s=1000, facecolors='none', edgecolors='b')
                plt.text(x, y, str(node.val), ha='center', va='center', fontsize=15)
                if node.left:
                    plt.plot([x-spacing, x], [y-1, y], color='gray', linewidth=1.5)
                    dfs(node.left, x-spacing, y-1, spacing/2)
                if node.right:
                    plt.plot([x+spacing, x], [y-1, y], color='gray', linewidth=1.5)
                    dfs(node.right, x+spacing, y-1, spacing/2)
        plt.figure(figsize=(8, 6))
        plt.axis('off')
        dfs(self, 0, 0, 1)
        plt.show()
                