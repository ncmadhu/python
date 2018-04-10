#Author: Madhu Chakravarthy
#Date: 09-04-2018
class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        root = self.buildMaximumTree(nums)
        return root

    def buildMaximumTree(self, nums):

        if not nums:
            return None

        maxNum = max(nums)
        maxIndex = nums.index(maxNum)

        node = TreeNode(maxNum)
        node.left = self.buildMaximumTree(nums[0:maxIndex])
        node.right = self.buildMaximumTree(nums[maxIndex+1:])
        return node

    def inOrderTraverse(self, node):

        def traverse(node, elements):
            if not node:
                return
            traverse(node.left, elements)
            elements.append(node.val)
            traverse(node.right, elements)

        elements = []
        traverse(node, elements)
        return elements

if __name__ == "__main__":
    sol = Solution()
    root = sol.constructMaximumBinaryTree([3,2,1,6,0,5])
    print sol.inOrderTraverse(root)
                
