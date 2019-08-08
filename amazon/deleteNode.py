#Author: Madhu Chakravarthy
#Date: 07-05-2018
class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution(object):
    def deleteNode(self, node):
        while node:
            node.val = node.next.val
            if node.next.next:
                node = node.next
            else:
                node.next = None
                node = None

    def buildList(self, values):
        head = curr = None
        for val in values:
            if curr:
                curr.next = ListNode(val)
                curr = curr.next
            else:
                curr = ListNode(val)
                head = curr
        return head

    def printList(self, head):
        curr = head
        while curr:
            print curr.val
            curr = curr.next

if __name__ == "__main__":
    sol =  Solution()
    head = sol.buildList([1,2,3,4,5])
    sol.printList(head)
    rdNode = head
    for i in range(2):
        rdNode = rdNode.next
    print rdNode.val
    sol.deleteNode(rdNode)
    sol.printList(head)




