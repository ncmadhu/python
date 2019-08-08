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

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root:
            if not root.left or root.right:
                return True
            else:
                return self.calculateHeight(root)
        else:
            return True

    def calculateHeight(self, node):

        if not node:
            return (0, True)

        leftHeight, leftState = self.calculateHeight(node.left)
        rightHeight, rightState = self.calculateHeight(node.right)
        height = max(leftHeight, rightHeight) + 1
        if leftState and rightState:
            if abs(leftHeight - rightHeight) < 2:
                return (height, True)
        return (height, False)

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
    print sol.isBalanced(bTree.root)



