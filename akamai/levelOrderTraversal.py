#Author: Madhu Chakravarthy
#Date: 19-04-2018
class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right =  None


def heightOfTree(root):

    if not root:
        return 0

    lHeight = heightOfTree(root.left)
    rHeight = heightOfTree(root.right)

    if lHeight > rHeight:
        return lHeight + 1
    else:
        return rHeight + 1

def levelOrderTraversal(root):

    if not root:
        return None

    queue = []

    queue.append(root)

    while queue:
        node = queue.pop(0)
        print node.val
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    print heightOfTree(root)
    levelOrderTraversal(root)
