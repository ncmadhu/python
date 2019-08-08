#Author: Madhu Chakravarthy
#Date: 09-04-2018
class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left =  None
        self.right = None

class BinaryTree(object):
    def __init__(self):
        self.root = None

    def insert(self, val):
        return self.insertNode(self.root, val)

    def insertNode(self, node, val):
        if not node:
            return TreeNode(val)

        if val > node.val:
            node.right = self.insertNode(node.right, val) 
        else:
            node.left = self.insertNode(node.left, val)

        return node

    def inOrderTraverse(self, root):

        def traverse(node, elements):
            if not node:
                return

            traverse(node.left, elements)
            elements.append(node.val)
            traverse(node.right, elements)

        elements = []
        traverse(root, elements)
        return elements


class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        nums = []
        self.getNumbers(root, nums, 0)
        return sum(nums)

    def getNumbers(self, node, nums, currSum):
        if node:
            if not node.left and not node.right:
                nums.append(currSum + node.val)
            if node.left:
                self.getNumbers(node.left, nums, (currSum + node.val) * 10)
            if node.right:
                self.getNumbers(node.right, nums, (currSum + node.val) * 10)


if __name__ == "__main__":
    bTree = BinaryTree()
    bTree.root = bTree.insertNode(bTree.root, 1)
    bTree.root.left = bTree.insertNode(bTree.root.left, 2)
    bTree.root.right = bTree.insertNode(bTree.root.right, 3)
    print bTree.inOrderTraverse(bTree.root)
    sol = Solution()
    print sol.sumNumbers(bTree.root)
