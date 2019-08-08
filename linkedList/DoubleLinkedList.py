# Author: Madhu Chakravarthy
# Date: 25-04-2017

class Node(object):

    def __init__(self, data):

        self.data = data
        self.previous = None
        self.next = None


    def getData(self):

        return self.data

    def setData(self,data):

        self.data = data

    def getPreviousNode(self):

        return self.previous

    def setPreviousNode(self, node):

        self.previous = node

    def getNextNode(self):

        return self.next

    def setNextNode(self, node):

        self.next = node


class DoubleLinkedList(object):

    def __init__(self,head=None):

        self.head = head


    def insertNode(self,data):

        node = Node(data)
        node.setNextNode(self.head)
        if self.head:
            self.head.setPreviousNode(node)
        self.head = node

    def size(self):

        current = self.head
        counter = 0

        while current:

            counter += 1
            current = current.getNextNode()

        return counter


    def deleteNode(self,data):

        current = self.head
        while current:

            if current.data == data:

                if current.next:
                    current.next.setPreviousNode(current.previous)

                if current.previous:
                    current.previous.setNextNode(current.next)
                else:
                    self.head = current.next
                break

            else:
                current = current.next

    def getAllNodes(self):

        current = self.head
        while current:
            if current.previous:
                print "Previous Data: {}".format(current.previous.data)
            print current.data
            if current.next:
                print "Next Data: {}".format(current.next.data)
            current = current.next

if __name__ == "__main__":

    dLinkedList = DoubleLinkedList()
    dLinkedList.insertNode("First")
    dLinkedList.insertNode("Second")
    dLinkedList.insertNode("Third")
    print dLinkedList.size()
    dLinkedList.getAllNodes()
    dLinkedList.deleteNode("Second")
    print dLinkedList.size()
    dLinkedList.getAllNodes()
    dLinkedList.deleteNode("Third")
    print dLinkedList.size()
    dLinkedList.getAllNodes()
    dLinkedList.insertNode("Second")
    dLinkedList.insertNode("Third")
    dLinkedList.deleteNode("First")
    print dLinkedList.size()
    dLinkedList.getAllNodes()
