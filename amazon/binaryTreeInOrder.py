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

    def inOrderTraversal2(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        elements = []
        stack = []
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left

            node = stack.pop()
            elements.append(node.val)
            curr = node.right

        return elements


if __name__ == "__main__":

    elements = [5, 2, 1, 3, 8, 7, 9, 6]
    bTree = BinaryTree()
    for element in elements:
        node = bTree.insert(element)
        #print node.val

    sol = Solution()
    elements = sol.inOrderTraversal(bTree.root)
    print elements

    elements = sol.inOrderTraversal2(bTree.root)
    print elements

    elements = [1,None,2,3]
    bTree = BinaryTree()
    for element in elements:
        node = bTree.insert(element)

    elements = sol.inOrderTraversal(bTree.root)
    print elements

    elements = sol.inOrderTraversal2(bTree.root)
    print elements
