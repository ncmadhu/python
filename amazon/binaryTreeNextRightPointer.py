#Author: Madhu Chakravarthy
#Date: 11-03-2018
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class BinaryTree(object):
    def __init__(self):
        self.root = None

class Solution(object):
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        def setNext(node1, node2):
            if node1:
                node1.next = node2
                setNext(node1.left, node1.right)
                if node2:
                    setNext(node1.right, node2.left)
                else:
                    setNext(node1.right, None)
        if root:
            root.next = None
            setNext(root.left, root.right)
            setNext(root.right, None)

    def connect2(self, root):
        while root:
            next = root.left
            while root and root.left:
                root.left.next = root.right
                root.right.next = root.next and root.next.left
                root = root.next
            root = next

if __name__ == "__main__":
    bTree = BinaryTree()
    bTree.root =  TreeNode(1)
    bTree.root.left = TreeNode(2)
    bTree.root.right = TreeNode(3)
    bTree.root.left.left = TreeNode(4)
    bTree.root.left.right = TreeNode(5)
    bTree.root.right.left = TreeNode(6)
    bTree.root.right.right = TreeNode(7)

    sol = Solution()
    sol.connect(bTree.root)
    print bTree.root.left.next.val
    print bTree.root.right.next
    print bTree.root.left.left.next.val
    print bTree.root.left.right.next.val
    print bTree.root.right.left.next.val
    print bTree.root.right.right.next


