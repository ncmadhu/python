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
        temp1 = temp2 = TreeNode(0)
        while root:
            while root:
                temp2.next = root.left
                temp2 = temp2.next or temp2
                temp2.next = root.right
                temp2 = temp2.next or temp2
                root = root.next
            root, temp2 = temp1.next, temp1

if __name__ == "__main__":
    bTree = BinaryTree()
    bTree.root =  TreeNode(1)
    bTree.root.left = TreeNode(2)
    bTree.root.right = TreeNode(3)
    bTree.root.left.left = TreeNode(4)
    bTree.root.left.right = TreeNode(5)
    bTree.root.right.right = TreeNode(7)

    sol = Solution()
    sol.connect(bTree.root)
    print bTree.root.left.next.val
    print bTree.root.right.next
    print bTree.root.left.left.next.val
    print bTree.root.left.right.next.val
    print bTree.root.right.right.next


