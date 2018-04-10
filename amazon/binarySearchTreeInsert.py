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
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if val > root.val:
            if root.right:
                self.insertIntoBST(root.right, val)
            else:
                root.right = TreeNode(val)
        elif val < root.val:
            if root.left:
                self.insertIntoBST(root.left, val)
            else:
                root.left = TreeNode(val)

        return self.levelOrderTraversal(root)

    def levelOrderTraversal(self, root):
        elements = []
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node:
                elements.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
        return elements

if __name__ == "__main__":
    bTree = BinaryTree()
    bTree.insert(10)
    bTree.insert(5)
    bTree.insert(7)
    bTree.insert(4)
    bTree.insert(2)
    bTree.insert(3)
    bTree.insert(1)
    sol = Solution()
    print sol.insertIntoBST(bTree.root, 6)
    bTree = BinaryTree()
    bTree.insert(4)
    bTree.insert(2)
    bTree.insert(7)
    bTree.insert(1)
    bTree.insert(3)
    print sol.insertIntoBST(bTree.root, 5)


