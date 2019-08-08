#Author: Madhu Chakravarthy
#Date: 07-05-2018
class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        nodes = []
        curr =  head
        prev = None
        while curr:
            nodes.append([curr, prev])
            prev =  curr
            curr = curr.next
        nthNodeFromEnd = nodes[-n]
        prev = nthNodeFromEnd[1]
        if prev:
            prev.next = nthNodeFromEnd[0].next
        else:
            head = nthNodeFromEnd[0].next

        return head

    def removeNthFromEnd2(self, head, n):
        dummyNode = ListNode(0)
        dummyNode.next = head
        first = second = dummyNode
        for i in range(n+1):
            first = first.next

        while first and second:
            first = first.next
            second = second.next

        second.next = second.next.next
        return dummyNode.next


    def buildList(self, arr):
        head = None
        curr = head
        for val in arr:
            if curr:
                curr.next = ListNode(val)
                curr = curr.next
            else:
                head = curr = ListNode(val)

        return head

    def printList(self, head):
        print "###########################"
        curr = head
        while curr:
            print curr.val
            curr = curr.next
        print "###########################"

if __name__ == "__main__":
    sol = Solution()
    arr = [1,2,3,4,5]
    head = sol.buildList(arr)
    sol.printList(head)
    head = sol.removeNthFromEnd(head, 2)
    sol.printList(head)
    head = sol.removeNthFromEnd2(head, 2)
    sol.printList(head)
    head = sol.removeNthFromEnd2(head, 3)
    sol.printList(head)
    head = sol.removeNthFromEnd2(head, 2)
    sol.printList(head)


            

