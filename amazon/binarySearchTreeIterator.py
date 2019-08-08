#Author: Madhu Chakravarthy
#Date: 24-03-2018
class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root == None:
            self.root = TreeNode(val)
        else:
            self.insertNode(val, self.root)

    def insertNode(self, val, node):
        if val > node.val:
            if node.right:
                self.insertNode(val, node.right)
            else:
                node.right = TreeNode(val)
        elif val < node.val:
            if node.left:
                self.insertNode(val, node.left)
            else:
                node.left = TreeNode(val)

class BSTIterator(object):
    def __init__(self, root):
        self.root = root
        self.elements = self.inOrder()

    def inOrder(self):
        elements = []
        def traverse(node, elements):
            if not node:
                return
            traverse(node.left, elements)
            elements.append(node.val)
            traverse(node.right, elements)

        traverse(self.root, elements)
        return elements

    def next(self):
        return self.elements.pop(0)

    def hasNext(self):
        return True if self.elements else False

if __name__ == "__main__":
    bTree = BinaryTree()
    bTree.insert(10)
    bTree.insert(5)
    bTree.insert(6)
    bTree.insert(4)
    bTree.insert(2)
    bTree.insert(3)
    bTree.insert(1)
    bstIter = BSTIterator(bTree.root)
    while bstIter.hasNext():
        print bstIter.next()


