#Author: Madhu Chakravarthy
#Date: 07-04-2018
class TreeNode(object):
    def __init__(self, val, parent, color):
        self.val = val
        self.left = None
        self.right =  None
        self.parent = parent
        self.color = color

class RedBlackBinarySearchTree(object):
    def __init__(self):
        self.root = None

    def createBlackNode(self, val):
        return TreeNode(val, None, 'BLACK')

    def createRedNode(self, val, parent):
        return TreeNode(val, parent, 'RED')

    def findSiblingNode(self, node):
        parent = node.parent
        if self.isLeftChild(node):
            return parent.right
        else:
            return parent.left

    def isLeftChild(self, node):
        if node.parent.left == node:
            return True
        else:
            return False

    def insert(self, root, val):
        return self.insertNode(val, root, None)

    def rotateRight(self, node, colorChange):
        parent = node.parent
        node.parent = parent.parent
        if parent.parent != None:
            if parent.parent.right == parent:
                parent.parent.right = node
            else:
                parent.parent.left = node
        right = node.right
        node.right = parent
        parent.parent = node
        parent.left = right
        if right:
            right.parent = parent
        if colorChange:
            node.color = "BLACK"
            parent.color = "RED"

    def rotateLeft(self, node, colorChange):
        parent = node.parent
        node.parent = parent.parent
        if parent.parent != None:
            if parent.parent.right == parent:
                parent.parent.right = node
            else:
                parent.parent.left = node

        left = node.left
        node.left = parent
        parent.parent = node
        parent.right = left
        if left:
            left.parent = parent
        if colorChange:
            node.color = "BLACK"
            parent.color ="RED"


    def insertNode(self, val, root, parent):
        if root == None:
            if parent == None:
                return self.createBlackNode(val)
            else:
                return self.createRedNode(val, parent)

        if root.val == val:
            raise Exception("Duplicate data not allowed")

        if root.val > val:
            left = self.insertNode(val, root.left, root)

            #if right rotation happened. left will become parent of root
            if left == root.parent:
                return left

            #set the left child of root as left
            root.left = left
            isLeft = True
        else:
            right = self.insertNode(val, root.right, root)

            #if left rotation happened. right will become parent of root
            if right == root.parent:
                return right

            root.right = right
            isLeft = False

        if isLeft:
            #check left side for red-red conflict between root and its left child
            if root.color == 'RED' and root.left.color == 'RED':
                # get the color of the root sibling
                sibling = self.findSiblingNode(root)
                #If sibling not present or sibling color is black
                if not sibling or sibling.color == 'BLACK':
                    #check for LeftLeft scenario
                    if self.isLeftChild(root):
                        #Rotate right
                        self.rotateRight(root, True)
                    else:
                        #LeftRight scenario
                        #Rotate RightLeft
                        self.rotateRight(root.left, False)
                        root = root.parent
                        self.rotateLeft(root, True)
                else:
                    #sibling is red color
                    root.color = "BLACK"
                    sibling.color = "BLACK"
                    #Check root parent is not Tree root node
                    if root.parent.parent != None:
                        root.parent.color = "RED"
        else:
            if root.color == "RED" and root.right.color == "RED":
                sibling = self.findSiblingNode(root)
                #If sibling is not present or sibling color is black
                if not sibling or sibling.color == "BLACK":
                    #RightLeft scenario check
                    if not self.isLeftChild(root):
                        self.rotateLeft(root, True)
                    else:
                       #RightLeftScenario
                       #Rotate LeftRight
                       self.rotateLeft(root.right, False)
                       root = root.parent
                       self.rotateRight(root, True)
                else:
                    root.color = "BLACK"
                    sibling.color = "BLACK"
                    if root.parent.parent != None:
                        root.parent.color = "RED"
        return root

    def printRedBlackTree(self, node, space):
        if node == None:
            print "%s%s %s" % (" " * space , "NULL", "NULL")
            return
        self.printRedBlackTree(node.right, space + 15)
        print "%s%s %s" % (" " * space , node.val, node.color)
        self.printRedBlackTree(node.left, space + 15)

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root:
            if root.left and root.right:
                return self.checkBalance(root)
        return True

    def calculateHeight(self, node):

        if not node:
            return 0

        leftHeight = self.calculateHeight(node.left)
        rightHeight = self.calculateHeight(node.right)
        return max(leftHeight, rightHeight) + 1

    def checkBalance(self, node):

        leftHeight = self.calculateHeight(node.left)
        rightHeight =  self.calculateHeight(node.right)

        if abs(leftHeight - rightHeight) > 1:
            return False
        return True

if __name__ == "__main__":
    redBlackTree = RedBlackBinarySearchTree()
    root = redBlackTree.root
    root = redBlackTree.insert(root, 10);
    root = redBlackTree.insert(root, 15);
    root = redBlackTree.insert(root, -10);
    root = redBlackTree.insert(root, 20);
    root = redBlackTree.insert(root, 30);
    root = redBlackTree.insert(root, 40);
    root = redBlackTree.insert(root, 50);
    root = redBlackTree.insert(root, -15);
    root = redBlackTree.insert(root, 25);
    root = redBlackTree.insert(root, 17);
    root = redBlackTree.insert(root, 21);
    root = redBlackTree.insert(root, 24);
    root = redBlackTree.insert(root, 28);
    root = redBlackTree.insert(root, 34);
    root = redBlackTree.insert(root, 32);
    root = redBlackTree.insert(root, 26);
    root = redBlackTree.insert(root, 35);
    root = redBlackTree.insert(root, 19);
    redBlackTree.printRedBlackTree(root, 5)
    print redBlackTree.isBalanced(root)


