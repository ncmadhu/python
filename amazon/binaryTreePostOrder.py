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
    def postOrderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        elements = []

        def traverse(root, elements):
            if root.left:
                traverse(root.left, elements)
            if root.right:
                traverse(root.right, elements)
            elements.append(root.val)

        traverse(root, elements)
        return elements

    def postOrderTraversal2(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        elements = []
        stack = [(1, root)]
        while stack:
            node = stack.pop()
            if node[1]:
                if node[0]:
                    stack.append((0, node[1]))
                    stack.append((1, node[1].right))
                    stack.append((1, node[1].left))
                else:
                    elements.append(node[1].val)

        return elements


if __name__ == "__main__":

    elements = [5, 2, 1, 3, 8, 7, 9, 6]
    bTree = BinaryTree()
    for element in elements:
        node = bTree.insert(element)
        #print node.val

    sol = Solution()
    elements = sol.postOrderTraversal(bTree.root)
    print elements

    elements = sol.postOrderTraversal2(bTree.root)
    print elements

    elements = [1,None,2,3]
    bTree = BinaryTree()
    for element in elements:
        node = bTree.insert(element)

    elements = sol.postOrderTraversal(bTree.root)
    print elements

    elements = sol.postOrderTraversal2(bTree.root)
    print elements
