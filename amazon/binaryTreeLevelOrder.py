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
    def levelOrderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        elements = []

        def traverse(nodes, elements):
            newNodes = []
            for elem in nodes:
                if elem:
                    elements.append(elem.val)
                    newNodes.append(elem.left)
                    newNodes.append(elem.right)
            if newNodes:
                traverse(newNodes, elements)

        traverse([root], elements)
        return elements

    def levelOrderTraversal2(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        elements = []
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node:
                elements.append(node.val)
                queue.append(node.left)
                queue.append(node.right)

        return elements

    def levelOrderTraversal3(self, root):
        elements = []
        queue = [[root]]
        while queue:
            result = []
            nodes = queue.pop(0)
            newNodes = []
            for node in nodes:
                if node:
                    result.append(node.val)
                    newNodes.append(node.left)
                    newNodes.append(node.right)
            if result:
                elements.append(result)
            if newNodes:
                queue.append(newNodes)
        return elements



if __name__ == "__main__":

    elements = [5, 2, 1, 3, 8, 7, 9, 6]
    bTree = BinaryTree()
    for element in elements:
        node = bTree.insert(element)
        #print node.val

    sol = Solution()
    elements = sol.levelOrderTraversal(bTree.root)
    print elements

    elements = sol.levelOrderTraversal2(bTree.root)
    print elements

    elements = sol.levelOrderTraversal3(bTree.root)
    print elements

    elements = [1,None,2,3]
    bTree = BinaryTree()
    for element in elements:
        node = bTree.insert(element)

    elements = sol.levelOrderTraversal(bTree.root)
    print elements

    elements = sol.levelOrderTraversal2(bTree.root)
    print elements
