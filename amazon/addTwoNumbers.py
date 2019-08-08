# Author: Madhu Chakravarthy
# Date: 05-02-2018

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        dummyHead = ListNode(0)
        curr = dummyHead
        carry = 0
        n1 = l1
        n2 = l2
        while n1 or n2 :
            x = n1.val if n1 else 0
            y = n2.val if n2 else 0
            sum = carry + x + y
            carry =  sum / 10
            curr.next = ListNode(sum % 10)
            curr = curr.next
            n1 = n1.next if n1 else n1
            n2 = n2.next if n2 else n2
        if carry > 0:
            curr.next = ListNode(carry)
        return dummyHead.next

if __name__ == "__main__":
    l1 = ListNode(0)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)
    l2 = ListNode(0)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
    sol = Solution()
    sum = sol.addTwoNumbers(l1, l2)
    while sum:
        print sum.val
        sum = sum.next
