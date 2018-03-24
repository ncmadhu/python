#Author: Madhu Chakravarthy
#Date: 08-03-2018
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        listALength = 0
        curr = headA
        while curr:
            listALength += 1
            curr = curr.next

        listBLength = 0
        curr = headB
        while curr:
            listBLength += 1
            curr = curr.next

        if listALength > listBLength:
            diff = listALength - listBLength
            for i in range(diff):
                headA = headA.next
        elif listBlength > listALength:
            diff = listBLength - listALength
            for i in range(diff):
                headB = headB.next

        while headA and headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        return None

if __name__ == "__main__":
    sol = Solution()
    headA = ListNode(1)
    curr = headA
    for i in range(2,6):
        curr.next = ListNode(i)
        curr = curr.next
    endA = curr
    headB = ListNode(1)
    curr = headB
    for i in range(2,4):
        curr.next = ListNode(i)
        curr = curr.next
    endB = curr
    headC = ListNode(66)
    curr = headC
    for i in range(7,9):
        curr.next = ListNode(i)
        curr = curr.next

    endA.next = headC
    endB.next = headC
    
    print sol.getIntersectionNode(headA, headB).val





