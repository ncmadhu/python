#!/bin/python
# Author: Madhu Chakravarthy
# Date: 21-12-2017

class Node:
    """
    class to instantiate a node
    """
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    """
    class to instantiate a binary tree
    """
    def __init__(self):
        self.root = None

    def addNode(self, value):
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

