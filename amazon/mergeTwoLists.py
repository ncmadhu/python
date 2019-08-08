#Author: Madhu Chakravarthy
#Date: 15-05-2018
class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next =  None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummyNode = ListNode(0)
        curr = dummyNode
        while l1 and l2:

            if l1.val > l2.val:
                curr.next = l2
                curr = l2
                l2 = l2.next
            else:
                curr.next = l1
                curr = l1
                l1 = l1.next

        while l1:
            curr.next = l1
            curr = l1
            l1 = l1.next

        while l2:
            curr.next = l2
            curr = l2
            l2 = l2.next

        return dummyNode.next

    def buildList(self, arr):
        dummyNode = ListNode(0)
        curr = dummyNode
        for val in arr:
            curr.next = ListNode(val)
            curr = curr.next

        return dummyNode.next

    def printList(self, head):
        print "###########################"
        curr = head
        while curr:
            print curr.val
            curr = curr.next
        print "###########################"

if __name__ == "__main__":
    sol = Solution()
    head1 = sol.buildList([1,2,4])
    sol.printList(head1)
    head2 = sol.buildList([1,3,4])
    sol.printList(head2)
    newHead = sol.mergeTwoLists(head1, head2)
    sol.printList(newHead)

                
