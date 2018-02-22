#!/bin/python
# Author: Madhu Chakravarthy
# Date: 21-12-2017

class Node:
    """
<<<<<<< HEAD
    class to create a node
=======
    class to instantiate a node
>>>>>>> 89d13cacaa013feb405f574e0881167c99aab14c
    """
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    """
<<<<<<< HEAD
    class to create a binary tree
    """
=======
    class to instantiate a binary tree
    """

>>>>>>> 89d13cacaa013feb405f574e0881167c99aab14c
    def __init__(self):
        self.root = None

    def addNode(self, value):
<<<<<<< HEAD
        self.add(self.root, value)

    def add(self, node, value):
        if node == None:
            self.root = Node(value)
        else:
            if value < node.data:
                self.addNode(value)
            elif value > node.data:
                self.addNode(value)

if __name__ == "__main__":

    binary_tree = BinaryTree() 
    binary_tree.addNode(10)
    binary_tree.data
    binary_tree.addNode(20)
    binary_tree.addNode(30)
    print binary_tree.root.left.data
    print binary_tree.root.right.data
=======
        return self.add(self.root, value)

    def add(self, node, value):
        if node == None:
            return Node(value)
        if value < node.data:
            if node.left:
                return self.add(node.left, value)
            else:
                node.left = Node(value)
                return node.left
        elif value > node.data:
            if node.right:
                return self.add(node.right, value)
            else:
                node.right = Node(value)
                return node.right

if __name__ == "__main__":
    binary_tree = BinaryTree()
    binary_tree.root = binary_tree.addNode(10)
    print binary_tree.root.data
    binary_tree.addNode(20)
    binary_tree.addNode(5)
    print binary_tree.root.left.data
    print binary_tree.root.right.data

>>>>>>> 89d13cacaa013feb405f574e0881167c99aab14c
