
from ABR import *
import matplotlib.pyplot as plt

def visualize(self):
        def dfs(node, x, y):
            if node:
                plt.scatter(x, y, s=1000, facecolors='none', edgecolors='b')
                plt.text(x, y, str(node.val), ha='center', va='center', fontsize=15)
                if node.left:
                    plt.plot([x-1, x], [y-1, y], color='gray', linewidth=1.5)
                    dfs(node.left, x-1, y-1)
                if node.right:
                    plt.plot([x+1, x], [y-1, y], color='gray', linewidth=1.5)
                    dfs(node.right, x+1, y-1)

        plt.figure(figsize=(8, 6))
        plt.axis('off')
        dfs(self, 0, 0)
        plt.show()