#Author: Madhu Chakravarthy
#Date: 17-04-2018

class TreeNode(object):
    def __init__(self, x):

        self.val = x
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self):
        self.root = None

    def insert(self, val):

        self.root = self.insertNode(self.root, val)
        return self.root

    def insertNode(self, root, val):

        if not root:
            return TreeNode(val)

        if root.val > val:
            root.left = self.insertNode(root.left, val)
        else:
            root.right = self.insertNode(root.right, val)

        return root

    def inOrderTraverse(self, root):

        def traverse(node, elements):
            if not node:
                return

            traverse(node.left, elements)
            elements.append(node.val)
            traverse(node.right, elements)

        elements = []
        traverse(root, elements)
        return elements


class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        numdict = {}
        return self.findTargetHelper(root, k, numdict)

    def findTargetHelper(self, node, tgt, numdict):
        if not node:
            return False
        if tgt - node.val in numdict:
            return True
        else:
            numdict[node.val] = 1
            result = self.findTargetHelper(node.left, tgt, numdict) or self.findTargetHelper(node.right, tgt, numdict)
            return result

if __name__ == "__main__":
    bTree = BinaryTree()
    bTree.insert(5)
    bTree.insert(6)
    bTree.insert(7)
    bTree.insert(3)
    bTree.insert(2)
    bTree.insert(4)
    print bTree.inOrderTraverse(bTree.root)
    sol =  Solution()
    print sol.findTarget(bTree.root, 9)
    print sol.findTarget(bTree.root, 19)


