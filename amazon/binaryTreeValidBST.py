#Author: Madhu Chakravarthy
#Date: 24-03-2018
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right =  None

class BinaryTree(object):
    def __init__(self):
        self.root =  None

    def insert(self, val):
        if self.root == None:
            self.root = TreeNode(val)
        else:
            self.insertNode(self.root, val)

    def insertNode(self, node, val):
        nodeVal = node.val
        if val > node.val:
            if node.right:
                self.insertNode(node.right, val)
            else:
                node.right = TreeNode(val)
        elif val < node.val:
            if node.left:
                self.insertNode(node.left, val)
            else:
                node.left = TreeNode(val)

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype boolean
        """
        output = []
        self.inOrder(root, output)
        for i in range(len(output) - 1):
            if output[i] > output[i+1]:
                return False
        return True

    def inOrder(self, root, output):
        if not root:
            return
        self.inOrder(root.left, output)
        output.append(root.val)
        self.inOrder(root.right, output)


if __name__ == "__main__":
    sol = Solution()
    bTree = BinaryTree()
    bTree.insert(2)
    bTree.insert(1)
    bTree.insert(3)
    print sol.isValidBST(bTree.root) 
