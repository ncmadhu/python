#Author: Madhu Chakravarthy
#Date: 11-03-2018
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self):
        self.root = None

class Solution(object):
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def countSingle(node, count):
            if node is None:
                return True

            left = countSingle(node.left, count)
            right = countSingle(node.right, count)

            if left == False or right == False:
                return False

            if node.left and node.val != node.left.val:
                return False

            if node.right and node.val != node.right.val:
                return False

            count[0] += 1
            return True

        count = [0]
        countSingle(root, count)
        return count[0]


if __name__ == "__main__":
    bTree = BinaryTree()
    bTree.root =  TreeNode(5)
    bTree.root.left = TreeNode(1)
    bTree.root.right = TreeNode(5)
    bTree.root.left.left = TreeNode(5)
    bTree.root.left.right = TreeNode(5)
    bTree.root.right.right = TreeNode(5)

    sol = Solution()
    print sol.countUnivalSubtrees(bTree.root)


