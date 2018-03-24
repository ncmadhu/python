#Author: Madhu Chakravarthy
#Date: 11-03-2018
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self):
        self.root = None

    def insertLeft(self, val):
        if self.root:
            curr = self.root
            while curr:
                if curr.left:
                    curr = curr.left
                else:
                    break
            curr.left = TreeNode(val)
        else:
            self.root = TreeNode(val)
            return self.root

    def insertRight(self, val):
        if self.root:
            curr = self.root
            while curr:
                if curr.right:
                    curr = curr.right
                else:
                    break
            curr.right = TreeNode(val)
        else:
            self.root = TreeNode(val)
            return self.root

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def compareChilds(node1, node2):
            if node1 and node2:
                if node1.val == node2.val:
                    symm1 = compareChilds(node1.left, node2.right)
                    symm2 = compareChilds(node1.right, node2.left)
                    return symm1 and symm2
                else:
                    return False
            elif not node1 and not node2:
                return True
            else:
                return False

        if root:
            return compareChilds(root.left, root.right)
        else:
            return True

    def isSymmetric2(self, root):
        queue = []
        queue.append(root)
        queue.append(root)

        while queue:
            n1 = queue.pop(0)
            n2 = queue.pop(0)
            if not n1 and not n2:
                continue
            if not n1 or not n2:
                return False
            if n1.val != n2.val:
                return False
            queue.append(n1.left)
            queue.append(n2.right)
            queue.append(n1.right)
            queue.append(n2.left)

        return True



if __name__ == "__main__":
    bTree = BinaryTree()
    bTree.root =  TreeNode(1)
    bTree.root.left = TreeNode(2)
    bTree.root.right = TreeNode(2)
    bTree.root.left.left = TreeNode(3)
    bTree.root.left.right = TreeNode(4)
    bTree.root.right.left = TreeNode(4)
    bTree.root.right.right = TreeNode(3)

    sol = Solution()
    print sol.isSymmetric(bTree.root)
    print sol.isSymmetric2(bTree.root)

    bTree = BinaryTree()
    bTree.root = TreeNode(1)
    bTree.root.left = TreeNode(2)
    bTree.root.right = TreeNode(2)
    bTree.root.left.right = TreeNode(3)
    bTree.root.right.right = TreeNode(3)

    sol = Solution()
    print sol.isSymmetric(bTree.root)
    print sol.isSymmetric2(bTree.root)


