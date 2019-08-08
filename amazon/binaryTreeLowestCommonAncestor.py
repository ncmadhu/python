#Author: Madhu Chakravarthy
#Date: 11-03-2018
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class BinaryTree(object):
    def __init__(self):
        self.root = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root:
            if root == p or root == q:
                return root
            lNode = self.lowestCommonAncestor(root.left, p, q)
            rNode = self.lowestCommonAncestor(root.right, p, q)
            if lNode and rNode:
                return root
            if not lNode and not rNode:
                return None
            return lNode if lNode else rNode
        else:
            return None

if __name__ == "__main__":
    bTree = BinaryTree()
    bTree.root =  TreeNode(3)
    bTree.root.left = TreeNode(5)
    bTree.root.right = TreeNode(1)
    bTree.root.left.left = TreeNode(6)
    bTree.root.left.right = TreeNode(2)
    bTree.root.right.left = TreeNode(0)
    bTree.root.right.right = TreeNode(8)
    bTree.root.left.right.left = TreeNode(7)
    bTree.root.left.right.right = TreeNode(4)

    sol = Solution()
    print sol.lowestCommonAncestor(bTree.root, bTree.root.left, bTree.root.right).val
    print sol.lowestCommonAncestor(bTree.root, bTree.root.left, bTree.root.left.right.right).val


