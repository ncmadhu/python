#Author: Madhu Chakravarthy
#Date: 08-03-2018
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype listNode
        """
        length = len(lists)

        if not lists or length == 0:
            return None
        elif length == 1:
            return lists[0]
        elif length == 2:
            return self.mergeTwoLists(lists[0], lists[1])
        else:
            mid = length / 2
            return self.mergeKLists([self.mergeKLists(lists[:mid]),
                                      self.mergeKLists(lists[mid:])])

    def mergeTwoLists(self, listA, listB):

        newList = ListNode(0)
        curr = newList

        while listA and listB:
            if listA.val <= listB.val:
                curr.next = listA
                listA = listA.next
                curr = curr.next
            else:
                curr.next = listB
                listB = listB.next
                curr = curr.next

        while listA:
            curr.next = listA
            listA = listA.next
            curr = curr.next

        while listB:
            curr.next = listB
            listB = listB.next
            curr = curr.next

        return newList.next

if __name__ == "__main__":

    sol = Solution()
    headA = ListNode(7)
    curr = headA
    for i in [9, 11, 13, 15, 17]:
        curr.next = ListNode(i)
        curr = curr.next

    headB = ListNode(6)
    curr = headB
    for i in [8, 10, 12, 14, 18]:
        curr.next = ListNode(i)
        curr = curr.next

    headC = ListNode(0)
    curr = headC
    for i in [1, 2, 2, 8, 9, 23]:
        curr.next = ListNode(i)
        curr = curr.next

    newList = sol.mergeKLists([headA, headB, headC])

    while newList:
        print newList.val
        newList = newList.next




