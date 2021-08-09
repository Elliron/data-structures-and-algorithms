from trees.tree import *

def fizz_buzz(self, K_Ary_Tree):
    new_tree = K_Ary_tree()
    while K_Ary_Tree.root:
        root = K_Ary_Tree.pop()
        if root is 15:
            root = 'FizzBuzz'
        if root is 3:
            root = 'Fizz'
        if root is 5:
            root = 'Buzz'
        else:
            root = str(root.value)
    new_tree.append(root)
    root = K_Ary_Tree.value.next
