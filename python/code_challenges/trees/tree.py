class Node:
    """
    Docstring
    """
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

class BinaryTree:
    """
    Docstring
    """
    def __init__(self):
        self.root = None

    def pre_order(self):
        # root >> left >> right
        res = []
        if self.root:
            res.append(self.root.value)
            res = res + self.pre_order(self.root.left)
            res = res + self.pre_order(self.root.right)

    def in_order(self):
        # left >> root >> right
        res = []
        if self.root:
            res = self.in_order(self.root.left)
            res.append(self.root.value)
            res = res + self.in_order(self.root.right)
        return res

    def post_order(self):
        # left >> right >> root
        res = []
        if self.root:
            res = self.post_order(self.root.left)
            res = res + self.post_order(self.root.right)
            res.append(self.root.value)

    def print_tree(self):
        if self.left:
            self.left.print_tree()
            print(self.value),
        if self.right:
            self.right.print_tree()




class BinarySearchTree(BinaryTree):
    """
    Docstring
    """

    def add(self, value):
        if self.value:
            if value < self.value:
                if self.left is None:
                    self.left = Node(value)
                else:
                    self.left.add(value)
            elif value > self.value:
                if self.right is None:
                    self.right = Node(value)
                else:
                    self.right.add(value)
        else:
            self.value = value

    def contains():
        pass


