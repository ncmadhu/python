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
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        while root:
            if val == root.val:
                return root
            elif val > root.val:
                root = root.right
            elif val < root.val:
                root = root.left

        return None
            


if __name__ == "__main__":
    bTree = BinaryTree()
    bTree.insert(10)
    bTree.insert(5)
    bTree.insert(6)
    bTree.insert(4)
    bTree.insert(2)
    bTree.insert(3)
    bTree.insert(1)
    sol = Solution()
    print sol.searchBST(bTree.root, 4)
    print sol.searchBST(bTree.root, 11)
    print sol.searchBST(bTree.root, 6)


