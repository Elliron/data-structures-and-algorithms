class Node:
    """
    Node for Binary Tree
    Node has a value and 2 nexts/children a left and a right

    """
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

class BinaryTree:
    """
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



class BinarySearchTree(BinaryTree):
    """
    Docstring
    """
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

