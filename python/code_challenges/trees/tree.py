class Node:
    """
<<<<<<< HEAD
    Node for Binary Tree
    Node has a value and 2 nexts/children a left and a right

=======
    Docstring
>>>>>>> c88b6a4c1f0f8b0d633e797f86f40eb179cd2e12
    """
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

class BinaryTree:
    """
<<<<<<< HEAD
    First node is the root
    preorder creates a tree copy
    in order gives nodes in non decreasing order
    post order deletes the tree

    """
    def __init__(self, root = None):
        self.root = root

    def pre_order(self):
        # root >> left >> right
        if self.root:
            print(self.root.value)

            self.pre_order(self.root.left)
            self.pre_order(self.root.right)


    def in_order(self):
        # left >> root >> right
        if self.root:
            self.in_order(self.root.left)
            print(self.root.value)
            self.in_order(self.root.right)

    def post_order(self):
        # left >> right >> root
        if self.root:
            self.in_order(self.root.left)
            self.in_order(self.root.right)
            print(self.root.value)
=======
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

>>>>>>> c88b6a4c1f0f8b0d633e797f86f40eb179cd2e12



class BinarySearchTree(BinaryTree):
    """
    Docstring
    """
<<<<<<< HEAD
    def __init__(self, root = None):
        self.root = root

    def add(self, value):
        if self.root is None:
            return Node(value)
        else:
            if self.root.value == value:
                return self.root
            elif self.root.value < value:
                self.root.right = self.add(self.root.right, value)
            else:
                self.root.left = self.add(self.root.left, value)
        return self.root




    def contains(self, value):
        if self.root is None or self.root.value == value:
            return self.root
        if self.root.value < value:
            return self.contains(self.root.right, value)
        return self.contains(self.root.left, value)

if __name__ == '__main__':

    tree = BinaryTree()
    tree.root = Node(1)
    tree.root.left = Node(6)
    tree.root.right = Node(10)
    tree.root.left.left = Node(8)
    tree.root.left.right = Node(12)
    tree.root.right.left = Node(23)
    tree.root.right.right = Node(28)

    tree.pre_order()
=======

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

>>>>>>> c88b6a4c1f0f8b0d633e797f86f40eb179cd2e12

