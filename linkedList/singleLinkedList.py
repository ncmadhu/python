# Author: Madhu Chakravarthy
# Date: 25-04-2017

class Node(object):

    def __init__(self, data):

        self.data = data
        self.next = None

    def getData(self):

        return self.data

    def setData(self, data):

        self.data = data

    def getNextNode(self):

        return self.next

    def setNextNode(self,node):

        self.next = node


class SingleLinkedList(object):

    def __init__(self, head=None):
        self.head = head

    def insertNode(self, data):

        node = Node(data)
        node.setNextNode(self.head)
        self.head = node

    def size(self):

        counter = 0
        node = self.head

        while node:
            counter += 1
            node = node.getNextNode()

        return counter


    def deleteNode(self,data):

        current = self.head
        previous = None

        while current:
            if current.data == data:
                if previous:
                    previous.setNextNode(current.getNextNode())
                else:
                    self.head = current.getNextNode()

                break
            else:
                previous = current
                current = current.getNextNode()

        return self.head


    def getAllNodes(self):

        current = self.head
        while current:
            print current.data
            current = current.getNextNode()





if __name__ == "__main__":

    sLinkedList = SingleLinkedList()
    sLinkedList.insertNode("First")
    sLinkedList.insertNode("Second")
    sLinkedList.insertNode("Third")
    print sLinkedList.size()
    sLinkedList.getAllNodes()
    sLinkedList.deleteNode("Second")
    print sLinkedList.size()
    sLinkedList.getAllNodes()
    sLinkedList.deleteNode("Third")
    print sLinkedList.size()
    sLinkedList.getAllNodes()
    sLinkedList.insertNode("Second")
    sLinkedList.insertNode("Third")
    sLinkedList.deleteNode("First")
    print sLinkedList.size()
    sLinkedList.getAllNodes()


