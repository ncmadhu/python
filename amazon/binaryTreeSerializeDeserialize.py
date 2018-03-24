#Author: Madhu Chakravarthy
#Date: 13-03-2018

#Definition for a binary tree node.
import ast
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self):
        self.root = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        elements = []
        def traverse(nodes, elements):
            newNodes = []
            for elem in nodes:
                if elem:
                    elements.append(elem.val)
                    newNodes.append(elem.left)
                    newNodes.append(elem.right)
                else:
                    elements.append(None)
            if newNodes:
                traverse(newNodes, elements)

        traverse([root], elements)
        return str(elements)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data:
            nodes = ast.literal_eval(data)
            root = TreeNode(nodes.pop(0))
            queue = [root]
            while queue:
                node = queue.pop(0)
                if not nodes:
                    break
                val =  nodes.pop(0)
                if val:
                    node.left = TreeNode(val)
                    queue.append(node.left)
                if not nodes:
                    break
                val =  nodes.pop(0)
                if val:
                    node.right = TreeNode(val)
                    queue.append(node.right)
            return root
        return None


       
if __name__ == "__main__":
    bTree = BinaryTree()
    bTree.root =  TreeNode(1)
    bTree.root.left = TreeNode(2)
    bTree.root.right = TreeNode(3)
    bTree.root.right.left = TreeNode(4)
    bTree.root.right.right = TreeNode(5)

    #Your Codec object will be instantiated and called as such:
    codec = Codec()
    #print codec.serialize(bTree.root)
    root = codec.deserialize(codec.serialize(bTree.root))
    print root.val
    print root.left.val
    print root.right.val
    print root.left.left
    print root.left.right
    print root.right.left.val
    print root.right.right.val
