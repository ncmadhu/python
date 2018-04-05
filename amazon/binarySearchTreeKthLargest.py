#Author: Madhu Chakravarthy
#Date: 10-03-2018
class TreeNode(object):
    def __init__(self, x, cnt=1):
        self.val = x
        self.cnt = cnt
        self.left = None
        self.right = None

class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.root = None
        self.k = k
        self.addNums(nums)

    def addNums(self, nums):
        for num in nums:
            self.add(num)
        

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if self.root == None:
            self.root = TreeNode(val)
        else:
            self.insert(val, self.root)

    def insert(self, val, node):

        nodeLeftCnt = node.left.cnt if node.left else 0
        nodeRightCnt = node.right.cnt if node.right else 0

        if val <= node.val:
            if node.left:
                self.insert(val, node.left)
            else:
                node.left = TreeNode(val)
            nodeLeftCnt = node.left.cnt
        elif val > node.val:
            if node.right:
                self.insert(val, node.right)
            else:
                node.right =  TreeNode(val)
            nodeRightCnt = node.right.cnt

        node.cnt = nodeLeftCnt + nodeRightCnt + 1

    def inOrderTraverse(self):

        def traverse(node, elements):
            if not node:
                return
            traverse(node.left, elements)
            elements.append(node.cnt)
            traverse(node.right, elements)

        elements = []
        traverse(self.root, elements)
        return elements

if __name__ == "__main__":
    kthLargest = KthLargest(3,[4,5,8,2])
    kthLargest.add(3);   # returns 4
    kthLargest.add(5);   # returns 5
    kthLargest.add(10);  # returns 5
    kthLargest.add(9);   # returns 8
    kthLargest.add(4);   # returns 8
    print kthLargest.inOrderTraverse()

