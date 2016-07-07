import sys

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
        
    def levelOrder(self,root):
        #Write your code here
        nodeValues = []
        self.collectNodeValues([root], nodeValues)
        nodeValues = map(str,nodeValues)
        print " ".join(nodeValues)
        
    def collectNodeValues(self,nodes, nodeValues):
        if nodes:
            newNodes = []
            for node in nodes:
                nodeValues.append(node.data)
                if node.left:
                    newNodes.append(node.left)
                if node.right:
                    newNodes.append(node.right)
            if newNodes:
                return self.collectNodeValues(newNodes, nodeValues)
            else:
                return newNodes
        else:
            return nodes
            
T=int(raw_input())
myTree=Solution()
root=None
for i in range(T):
    data=int(raw_input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)