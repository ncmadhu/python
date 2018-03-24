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
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        def checkSum(node, total, sum):
            if node:
                total += node.val
                if total == sum:
                    return True
                else:
                    leftRes = checkSum(node.left, total, sum)
                    if leftRes:
                        return True
                    rightRes = checkSum(node.right, total, sum)
                    if rightRes:
                        return True
            return False

        total = 0
        return checkSum(root, total, sum)

if __name__ == "__main__":
    bTree = BinaryTree()
    bTree.root =  TreeNode(5)
    bTree.root.left = TreeNode(4)
    bTree.root.right = TreeNode(8)
    bTree.root.left.left = TreeNode(11)
    bTree.root.left.left.left = TreeNode(7)
    bTree.root.left.left.right = TreeNode(2)
    bTree.root.right.left = TreeNode(13)
    bTree.root.right.right = TreeNode(4)
    bTree.root.right.right.right = TreeNode(1)

    sol = Solution()
    print sol.hasPathSum(bTree.root, 22)
    print sol.hasPathSum(bTree.root, 27)
    print sol.hasPathSum(bTree.root, 18)
    print sol.hasPathSum(bTree.root, 1)


