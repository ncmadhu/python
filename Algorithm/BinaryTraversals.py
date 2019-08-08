#!/bin/python
# Author: Madhu Chakravarthy
# Date: 1-1-2018

class Node:
    """
    Node of a binary tree
    """
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    """
    Binary Tree
    """
    def __init__(self):
        self.root = None

    def insert(self, data, node=None):
        if node == None:
            if self.root == None:
                self.root = Node(data)
                return self.root
            else:
                node = self.root
        if data < node.data:
            if node.left == None:
                node.left = Node(data)
            else:
                return self.insert(data, node.left)
        elif data > node.data:
            if node.right == None:
                node.right = Node(data)
            else:
                return self.insert(data, node.right)

    def inorderTraversal(self, node):
        """
        1. Traverse the left subtree
        2. Visit root
        3. Traverse the right subtree
        use: To Find elements in a tree. Gives elements in non-decreasing order
        """
        
        if node != None:
            if node.left != None:
                self.inorderTraversal(node.left)
            print node.data
            if node.right != None:
                self.inorderTraversal(node.right)

    def preorderTraversal(self, node):
        """
        1. Visit the root
        2. Traverse the left subtree
        3. Traverse the right subtree
        use: To take copy of a tree
        """

        if node != None:
            print node.data
            if node.left != None:
                self.preorderTraversal(node.left)
            if node.right != None:
                self.preorderTraversal(node.right)

    def postorderTraversal(self, node):
        """
        1. Traverse the left subtree
        2. Traverse the right subtree
        3. Visit root
        use: To delete an tree
        """

        if node != None:
            if node.left != None:
                self.postorderTraversal(node.left)
            if node.right != None:
                self.postorderTraversal(node.right)
            print node.data

    def find(self, data, node):

        if node != None:
            if data ==  node.data:
                return node
            elif data < node.data:
                return self.find(data, node.left)
            elif data > node.data:
                return self.find(data, node.right)
        else:
            return None

    def delete(self, data, node):
        pass
        


if __name__ == "__main__":
    binaryTree = BinaryTree()
    root = binaryTree.insert(25)
    child = binaryTree.insert(15)
    childR = binaryTree.insert(22, child)
    childL = binaryTree.insert(10, child)
    binaryTree.insert(24, childR)
    binaryTree.insert(18, childR)
    binaryTree.insert(4, childL)
    binaryTree.insert(12, childL)
    child = binaryTree.insert(50)
    childR = binaryTree.insert(70, child)
    childL = binaryTree.insert(35, child)
    binaryTree.insert(90, childR)
    binaryTree.insert(66, childR)
    binaryTree.insert(44, childL)
    binaryTree.insert(31, childL)
    print "#" * 30
    print "Inorder Traversal"
    print "#" * 30
    binaryTree.inorderTraversal(root)
    print "#" * 30
    print "Preorder Traversal"
    print "#" * 30
    binaryTree.preorderTraversal(root)
    print "#" * 30
    print "Postorder Traversal"
    print "#" * 30
    binaryTree.postorderTraversal(root)
    print "#" * 30
    print "Element search"
    print "#" * 30
    print binaryTree.find(45, root)
    print binaryTree.find(44, root)
    print binaryTree.find(4, root)
    print binaryTree.find(24, root)





