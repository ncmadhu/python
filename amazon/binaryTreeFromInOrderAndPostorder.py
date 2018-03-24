#Author: Madhu Chakravarthy
#Date: 11-03-2018
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not inorder or not postorder:
            return None

        root = TreeNode(postorder.pop())
        rootIndex = inorder.index(root.val)

        root.right = self.buildTree(inorder[rootIndex+1:], postorder)
        root.left =  self.buildTree(inorder[:rootIndex], postorder)

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
    inorder =  [9,3,15,20,7]
    postorder = [9,15,7,20,3]

    root = sol.buildTree(inorder, postorder)
    print sol.inOrderTraversal(root)
