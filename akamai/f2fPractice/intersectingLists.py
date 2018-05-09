#Author: Madhu Chakravarthy
#Date: 01-05-2018
class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

def buildList(arr):
    head = None
    curr = head
    for elem in arr:
        if curr:
            curr.next = Node(elem)
            curr = curr.next
        else:
            head = Node(elem)
            curr = head
    return head

def buildIntersectingList(head1, head2, intersectIndex):
    tail = head1

    while tail.next:
        tail = tail.next

    i = 0
    intersectNode = head2
    while i < intersectIndex and intersectNode.next:
        intersectNode = intersectNode.next
        i += 1

    tail.next = intersectNode

def findIntersection(head1, head2):

    list1Length = listLength(head1)
    list2Length = listLength(head2)

    if list1Length < list2Length:
        head1, head2 = head2, head1
        list1Length, list2Length = list2Length, list1Length

    diff = list1Length - list2Length
    i = 0
    while i < diff:
        head1 = head1.next
        i += 1

    while head1 and head2:

        if head1 == head2:
            return head1

        head1 = head1.next if head1 else None
        head2 = head2.next if head2 else None

    return None

def listLength(head):

    length = 0
    curr = head
    while curr:
        length += 1
        curr = curr.next
    return length

def buildLoopList(head1, head2):
    tail = head1
    while tail.next:
        tail = tail.next

    tail.next = head2

def detectLoop(head):

    slow = head
    fast = head
    while slow and fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return detectLoopStart(slow, head)
    return None

def detectLoopStart(node, head):

    ptr1 = node
    ptr2 = node
    k = 1

    while ptr1.next != ptr2:
        ptr1 = ptr1.next
        k += 1

    ptr1 = head
    ptr2 = head
    for i in range(k):
        ptr1 = ptr1.next

    while ptr1 != ptr2:
        ptr1 = ptr1.next
        ptr2 = ptr2.next

    return ptr1

def printList(head):
    print "######################"
    curr = head
    while curr:
        print curr.val
        curr = curr.next
    print "######################"

if __name__ == "__main__":
    head1 = buildList([1,2,3,4,5,6])
    printList(head1)
    head2 = buildList([7,8,9,10])
    printList(head2)
    buildIntersectingList(head1, head2, 2)
    printList(head1)

    intersectingNode = findIntersection(head1, head2)
    print intersectingNode.val

    buildLoopList(head1, head2)
    loopStart = detectLoop(head1)
    print loopStart.val
