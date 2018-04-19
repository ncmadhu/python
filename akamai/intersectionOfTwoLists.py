#Author: Madhu Chakravarthy
#Date: 18-04-2018
class Node(object):
    def __init__(self, val):
        self.val = val
        self.next =  None

def buildList(items):
    curr = None
    head = None
    for item in items:
        if head == None:
            head = Node(item)
            curr = head
        else:
            curr.next = Node(item)
            curr = curr.next

    return head

def buildIntersectingList(list1, list2, intersectIndex):
    head1 = buildList(list1)
    i = 0
    curr1 = head1
    while i < intersectIndex:
        curr1 = curr1.next
        i += 1
    head2 = buildList(list2)
    curr2 = head2
    while curr2.next:
        curr2 = curr2.next

    curr2.next = curr1
    return (head1, head2)

def findIntersection(listA, listB):

    listALen = 0
    currA = listA
    while currA:
        currA = currA.next
        listALen += 1

    listBLen = 0
    currB = listB
    while currB:
        currB = currB.next
        listBLen += 1
    headA = listA
    headB = listB
    if listALen > listBLen:
        diff = listALen - listBLen
        i = 0
        while i < diff:
            headA = headA.next
    else:
        diff = listBLen - listALen
        i = 0
        while i < diff:
            headB = headB.next
            i += 1

    while headA and headB:
        if headA == headB:
            return headA
        headA = headA.next
        headB = headB.next
    return None

if __name__ == "__main__":
    headA, headB = buildIntersectingList([4,5,6,7,8,9],[1,2,3],0)
    print headA.val
    print headB.val
    intersectingNode = findIntersection(headA, headB)
    print intersectingNode.val
