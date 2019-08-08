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

    def deleteNode(self, head, val):
        prev = None
        curr = head
        while curr:
            if curr.val == val:
                if curr.next:
                    if prev:
                        prev.next = curr.next
                        break
                    else:
                        return curr.next
                else:
                    if prev:
                        prev.next = None
                        break
                    else:
                        return None
            else:
                prev = curr
                curr = curr.next
        return head


if __name__ == "__main__":
    sol = Solution()
    head = sol.buildList([1,2,3,4,5])
    sol.printList(head)
    head = sol.deleteNode(head, 5)
    sol.printList(head)
    head = sol.deleteNode(head, 1)
    sol.printList(head)
    head = sol.deleteNode(head, 3)
    sol.printList(head)
    head = sol.deleteNode(head, 4)
    sol.printList(head)
    head = sol.deleteNode(head, 2)
    sol.printList(head)



