import matplotlib.pyplot as plt

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        # Compare the new value with the parent node
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
    
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data)
        if self.right:
            self.right.PrintTree()
    
    # Inorder traversal
    # Left -> Root -> Right
    def inorderTraversal(self, root):
        res = []
        if root:
            res = self.inorderTraversal(root.left)
            res.append(root.data)
            res = res + self.inorderTraversal(root.right)
        return res
    
    # Preorder traversal
    # Root -> Left -> Right
    def PreorderTraversal(self, root):
        res = []
        if root:
            res.append(root.data)
            res = res + self.PreorderTraversal(root.left)
            res = res + self.PreorderTraversal(root.right)
        return res

    def get_tree_plot(self, ax, x, y, dx, dy):
        ax.text(x, y, str(self.data), style='italic', bbox={'facecolor': 'red', 'alpha': 0.5, 'pad': 10})
        if self.left:
            ax.plot([x, x - dx], [y - dy, y + dy], 'k-')
            self.left.get_tree_plot(ax, x - dx, y + dy, dx / 2, dy)
        if self.right:
            ax.plot([x, x + dx], [y - dy, y + dy], 'k-')
            self.right.get_tree_plot(ax, x + dx, y + dy, dx / 2, dy)

    def plot_tree(self):
        fig, ax = plt.subplots()
        self.get_tree_plot(ax, 0.5, 1, 0.5, 0.5)
        ax.set_xlim([0, 1])
        ax.set_ylim([0, 1])
        ax.axis('off')
        plt.show()


root = Node(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)
root.plot_tree()
