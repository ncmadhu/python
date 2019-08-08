#Author: Madhu Chakravarthy
#Date: 01-05-2018

class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution(object):
    def buildList(self, arr):

        head = curr = None

        for elem in arr:
            if curr:
                curr.next = ListNode(elem)
                curr = curr.next
            else:
                curr = ListNode(elem)
                head = curr

        return head


    def printList(self, head):

        print "#####################"

        while head:
            print head.val
            head = head.next

        print "#####################"

    def reverseList(self, head):
        prev = None
        curr = head
        while curr:
            if prev:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            else:
                prev =  curr
                temp = curr.next
                curr.next = None
                curr = temp

        return prev



if __name__ == "__main__":
    sol = Solution()
    head = sol.buildList([1,2,3,4,5])
    sol.printList(head)
    head = sol.reverseList(head)
    sol.printList(head)



