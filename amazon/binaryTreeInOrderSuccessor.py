#Author: Madhu Chakravarthy
#Date: 24-03-2018
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right =  None

class BinaryTree(object):
    def __init__(self):
        self.root =  None

    def insert(self, val):
        if self.root == None:
            self.root = TreeNode(val)
            return self.root
        else:
            return self.insertNode(self.root, val)

    def insertNode(self, node, val):
        nodeVal = node.val
        if val > node.val:
            if node.right:
                return self.insertNode(node.right, val)
            else:
                node.right = TreeNode(val)
                return node.right
        elif val < node.val:
            if node.left:
                return self.insertNode(node.left, val)
            else:
                node.left = TreeNode(val)
                return node.left

class Solution(object):
    def inOrderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :rtype boolean
        """
        nodes = []
        def traverse(node, nodes):
            if not node:
                return

            traverse(node.left, nodes)
            nodes.append(node)
            traverse(node.right, nodes)

        traverse(root, nodes)
        length = len(nodes)

        for index, node in enumerate(nodes):
            if node == p:
                return nodes[index+1] if index+1 < length else None

        return None

    def inOrderSuccessor2(self, root, p):
        if p.right:
            p = p.right
            while p.left:
                p = p.left
            return p

        treeNode = None

        while root != p:
            if p.val > root.val:
                root = root.right
            else:
                treeNode = root
                root = root.left

        return treeNode

if __name__ == "__main__":
    sol = Solution()
    bTree = BinaryTree()
    bTree.insert(25)
    bTree.insert(10)
    n1 = bTree.insert(5)
    bTree.insert(18)
    bTree.insert(23)
    n2 = bTree.insert(19)
    print sol.inOrderSuccessor(bTree.root, n1).val 
    print sol.inOrderSuccessor2(bTree.root, n1).val 
    print sol.inOrderSuccessor(bTree.root, n2).val 
    print sol.inOrderSuccessor2(bTree.root, n2).val 
