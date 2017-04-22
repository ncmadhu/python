# Author: Madhu Chakravarthy
# Date: 22-04-2017

'''
Level Order Traversal:
 Traversing all nodes at a given level
 1. Initialize nodes
 2. Find Max height of tree from root - longest path from root

'''

class Node(object):

    def __init__(self, data):

        self.data = data
        self.left = None
        self.right = None



def heightOfTree(node):

    if node is None:
        return 0
    else:
        lheight = heightOfTree(node.left)
        rheight = heightOfTree(node.right)

        if lheight > rheight:
            return lheight + 1
        else:
            return rheight + 1

def printAllNodes(root):

    height = heightOfTree(root)
    for i in range(1, height + 1):
        printNodesAtGivenLevel(root,i)

def printNodesAtGivenLevel(root, level):

    if root is None:
        return
    if level == 1:
        print root.data
    elif level > 1:
        printNodesAtGivenLevel(root.left, level -1)
        printNodesAtGivenLevel(root.right, level -1)

if __name__ == "__main__":

    node = Node(1)
    node.left = Node(2)
    node.right = Node(3)
    node.left.left = Node(4)
    node.left.right = Node(5)

    #printNodesAtGivenLevel(node,3)
    printAllNodes(node)
