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

class Solution(object):

    def getInOrderSuccessor(self, node):
        successor = node.right
        parent = node
        while successor and successor.left:
            parent = successor
            successor = successor.left
        return successor, parent

    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        dummyRoot = TreeNode(0)
        parent = dummyRoot
        dummyRoot.left = root
        current = root

        while current  and current.val != key:
            parent = current
            if current.val < key:
                current = current.right
            else:
                current = current.left

        if current and current.val == key:
            if current.left and current.right:
                successor, parent = self.getInOrderSuccessor(current)
                current.val = successor.val
                current = successor

            child = current.left if current.left else current.right
            if parent.left == current:
                parent.left = child
            else:
                parent.right = child

        return dummyRoot.left

    def inOrderTraverse(self, root):

        elements = []

        def traverse(node, elements):
            if not node:
                return
            traverse(node.left, elements)
            elements.append(node.val)
            traverse(node.right, elements)

        traverse(root, elements)
        return elements



            

if __name__ == "__main__":
    bTree = BinaryTree()
    bTree.insert(10)
    bTree.insert(5)
    bTree.insert(6)
    bTree.insert(4)
    bTree.insert(2)
    bTree.insert(3)
    bTree.insert(1)
    bTree.insert(8)
    sol = Solution()
    print sol.inOrderTraverse(bTree.root)
    root = sol.deleteNode(bTree.root, 2)
    print sol.inOrderTraverse(root)
    root = sol.deleteNode(root, 10)
    print sol.inOrderTraverse(root)


