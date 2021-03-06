class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
        
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root
        
    def getHeight(self,root):
        #Write your code here
        left_length = 0
        right_length = 0
        if root.left:
            left_length += 1 + self.getHeight(root.left)
        if root.right:
            right_length += 1 + self.getHeight(root.right)
        return max(left_length, right_length)
        
T=int(raw_input())
myTree=Solution()
root=None
for i in range(T):
    data=int(raw_input())
    root=myTree.insert(root,data)
height=myTree.getHeight(root)
print height