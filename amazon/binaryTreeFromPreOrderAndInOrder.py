#Author: Madhu Chakravarthy
#Date: 11-03-2018
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not inorder or not preorder:
            return None

        root = TreeNode(preorder.pop(0))
        rootIndex = inorder.index(root.val)

        root.left =  self.buildTree(preorder, inorder[:rootIndex])
        root.right = self.buildTree(preorder, inorder[rootIndex+1:])

        return root

    def inOrderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        elements = []

        def traverse(root, elements):
            if root.left:
                traverse(root.left, elements)
            elements.append(root.val)
            if root.right:
                traverse(root.right, elements)

        traverse(root, elements)
        return elements


if __name__ == "__main__":
    sol = Solution()
    preorder = [3,9,20,15,7]
    inorder =  [9,3,15,20,7]

    root = sol.buildTree(preorder, inorder)
    print sol.inOrderTraversal(root)
