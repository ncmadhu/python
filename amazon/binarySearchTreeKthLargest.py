#Author: Madhu Chakravarthy
#Date: 10-03-2018
class TreeNode(object):
    def __init__(self, x, cnt=1):
        self.val = x
        self.cnt = cnt
        self.left = None
        self.right = None

class MyKthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.root = None
        self.k = k
        self.insertNums(nums)

    def insertNums(self, nums):
        if self.root == None:
            self.root =  TreeNode(nums.pop(0))
        for num in nums:
            self.insert(num, self.root)
        
    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        self.insert(val, self.root)
        return self.kthLargest()

    def kthLargest(self):
        def kHelper(node, k, kthLargest):
            #import pdb
            #pdb.set_trace()
            if not node or k[0] >= self.k:
                return False
            kHelper(node.right,k,kthLargest)
            k[0] = k[0] + 1
            if k[0] == self.k:
                kthLargest.insert(0, node.val)
                return True
            kHelper(node.left, k, kthLargest)

        kthLargest = []
        k= [0]
        kHelper(self.root, k, kthLargest)
        return kthLargest[0]


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
            elements.append(node.val)
            traverse(node.right, elements)

        elements = []
        traverse(self.root, elements)
        return elements

class KthLargest(object):
    def __init__(self, k, nums):
        self.root = None
        self.k = k
        for num in nums:
            self.root = self.insertNode(num, self.root)

    def insertNode(self, val, node):
        if node == None:
            return TreeNode(val)
        if node.val < val:
                node.right = self.insertNode(val, node.right)
        else:
                node.left = self.insertNode(val, node.left)
        node.cnt += 1
        return node

    def add(self, val):
        node = self.insertNode(val, self.root)
        return self.searchKthLargest(self.root, self.k)

    def searchKthLargest(self, node, k):

        m = node.right.cnt if node.right else 0
        if k == m + 1:
            return node.val
        if k <= m:
            return self.searchKthLargest(node.right, k)
        else:
            return self.searchKthLargest(node.left, k - m - 1)
            

if __name__ == "__main__":
    kthLargest = KthLargest(3,[4,5,8,2])
    print kthLargest.add(3);   # returns 4
    print kthLargest.add(5);   # returns 5
    print kthLargest.add(10);  # returns 5
    print kthLargest.add(9);   # returns 8
    print kthLargest.add(4);   # returns 8
    kthLargest = KthLargest(4,[5,2,6,7,4,3,1])

