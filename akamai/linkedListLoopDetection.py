#Author: Madhu Chakravarthy
#Date: 18-04-2018
class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

def buildList(items):
    head = None
    curr = None
    for item in items:
        if head == None:
            head = Node(item)
            curr = head
        else:
            curr.next = Node(item)
            curr = curr.next
    return head

def buildIntersectingList(listA, listB, intersectIndex):

    headA = buildList(listA)
    currA = headA
    i = 0
    while i < intersectIndex:
        currA = currA.next
        i += 1
    headB = buildList(listB)
    currB = headB
    while currB.next:
        currB = currB.next
    currB.next = currA

    return (headA, headB)

def buildLoopList(listA, listB):
    currA = listA
    while currA.next:
        currA =  currA.next

    currA.next = listB

def listLength(listHead):
    i = 0
    curr = listHead
    while curr:
        curr = curr.next
        i += 1
    return i

def findIntersection(listA, listB):

    headA = listA
    headB = listB
    listALength = listLength(headA)
    listBLength = listLength(headB)
    if listALength > listBLength:
        diff = listALength - listBLength
        for i in range(diff):
            headA =  headA.next
    else:
        diff = listBLength - listALength
        for i in range(diff):
            headB = headB.next

    while headA and headB:
        if headA == headB:
            return headA
        headA = headA.next
        headB = headB.next
    return None

def detectLoopStart(head):
    slow = head
    fast = head
    while slow and fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return startOfLoop(slow, head)
    return None

def startOfLoop(node, head):
    ptr1 = node
    ptr2 = node
    k = 1
    while ptr1.next != ptr2:
        ptr1 = ptr1.next
        k += 1

    ptr1 = head
    ptr2 = head
    for i in range(k):
        ptr2 = ptr2.next

    while ptr1 != ptr2:
        ptr1 = ptr1.next
        ptr2 = ptr2.next

    return ptr1



if __name__ == "__main__":
    headA, headB = buildIntersectingList([4,5,6,7,8,9],[1,2,3],2)
    print headA.val
    print headB.val
    intersectingNode = findIntersection(headA, headB)
    print intersectingNode.val
    buildLoopList(headA, headB)
    loopStart = detectLoopStart(headA)
    print loopStart.val
