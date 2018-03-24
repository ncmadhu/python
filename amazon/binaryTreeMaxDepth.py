#Author: Madhu Chakravarthy
#Date: 10-03-2018
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self):
        self.root = None

    def insert(self, x):
        return self.insertNode(x, self.root)


    def insertNode(self, x, node):
        if node:
            if x > node.val:
                if node.right:
                    return self.insertNode(x, node.right)
                else:
                    node.right = TreeNode(x)
                    return node.right
            else:
                if node.left:
                    return self.insertNode(x, node.left)
                else:
                    node.left = TreeNode(x)
                    return node.left
        else:
            self.root = TreeNode(x)
            return self.root

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def findDepth(root, depth):
            lDepth = findDepth(root.left, depth+1) if root.left else depth
            rDepth = findDepth(root.right, depth+1) if root.right else depth
            return max(lDepth, rDepth)

        depth = 0

        return findDepth(root, depth+1) if root else depth




if __name__ == "__main__":

    elements = [5, 2, 1, 3, 8, 7, 9, 6]
    bTree = BinaryTree()
    for element in elements:
        node = bTree.insert(element)

    sol = Solution()
    depth = sol.maxDepth(bTree.root)
    print depth

    elements = [1,None,2,3]
    bTree = BinaryTree()
    for element in elements:
        node = bTree.insert(element)

    depth = sol.maxDepth(bTree.root)
    print depth

