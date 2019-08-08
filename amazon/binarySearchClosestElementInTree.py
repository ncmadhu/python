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
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        return self.closestElemFind(root, target)

    def closestElemFind(self, node, target):

        if not node:
            return None

        val = node.val
        if val == target:
            return val
        elif val < target:
            ret_val = self.closestElemFind(node.right, target)
        else:
            ret_val = self.closestElemFind(node.left, target)

        if ret_val:
            if ret_val == target:
                return ret_val
            elif abs(ret_val - target) <= abs(val - target):
                return ret_val
        return val
            

if __name__ == "__main__":

    sol = Solution()

    elements = [5, 2, 1, 3, 8, 7, 9, 6]
    bTree = BinaryTree()
    for element in elements:
        node = bTree.insert(element)

    print sol.closestValue(bTree.root, 4)
    print sol.closestValue(bTree.root, 9)

    elements = [9,4,17,3,6,5,7,22,20]
    bTree = BinaryTree()
    for element in elements:
        node = bTree.insert(element)

    print sol.closestValue(bTree.root, 4)
    print sol.closestValue(bTree.root, 18)
    print sol.closestValue(bTree.root, 12)
