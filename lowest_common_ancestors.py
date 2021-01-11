class Node:
    def __init__(self,left=None, right=None):
        self.value = None
        self.left = left
        self.right = right

    def add(self,node):
        a = self.left is None
        b = self.right is None
        if a and b:
            import random
            if random.random() < 0.5:
                self.left = node
            else:
                self.right = node
        elif a:
            self.left = node
        elif b:
            self.right = node
        else:
            import random
            if random.random() < 0.5:
                self.right.add(node)
            else:
                self.left.add(node)



class Tree:
    def __init__(self,root):
        self.root = root

    def add(self,node):
        self.root.add(node)




def solve():
    pass


root = Node()
tree = Tree(root)
tree.add(Node())
