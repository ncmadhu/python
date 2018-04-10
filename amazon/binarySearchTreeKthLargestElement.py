#Author: Madhu Chakravarthy
#Date: 24-03-2018
class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.kthlargest = 1
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

class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.root = BinaryTree()
        for num in nums:
            self.add(num)
        

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
            

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


