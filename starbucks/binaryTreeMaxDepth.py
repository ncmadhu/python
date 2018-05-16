#Author: Madhu Chakravarthy
#Date: 15-05-2018
class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root:
            self.insertNode(self.root, val)
        else:
            self.root = TreeNode(val)

    def insertNode(self, node, val):
        if node:
            if node.val > val:
                node.left = self.insertNode(node.left, val)
            else:
                node.right = self.insertNode(node.right, val)
        else:
            node =  TreeNode(val)

        return node

    def levelOrderTraversal(self, root):
        if root:
            queue = [root]
        print "#########################"
        while queue:
            node = queue.pop(0)
            if node:
                print node.val
                queue.append(node.left)
                queue.append(node.right)
        print "#########################"

class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0
        def helper(node, currDepth):
            if not node:
                return currDepth
            leftDepth = helper(node.left, currDepth+1)
            rightDepth = helper(node.right, currDepth+1)
            return max(leftDepth, rightDepth)

        return helper(root, 0)

if __name__ == "__main__":
    bTree = BinaryTree()
    bTree.insert(6)
    bTree.insert(8)
    bTree.insert(4)
    bTree.insert(5)
    bTree.insert(3)
    bTree.insert(2)
    bTree.insert(7)
    bTree.insert(9)
    bTree.levelOrderTraversal(bTree.root)
    sol = Solution()
    print sol.maxDepth(bTree.root)

