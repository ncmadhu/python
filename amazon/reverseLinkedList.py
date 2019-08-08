#Author: Madhu Chakravarthy
#Date: 07-05-2018
class ListNode(object):
    def __init__(self, val):
        self.val =  val
        self.next =  None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        curr = head
        while curr:
            if prev:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr =  temp
            else:
                prev =  curr
                temp = curr.next
                curr.next = None
                curr = temp

        return prev

    def reverseListRecursive(self, head):

        def recurse(node, prevNode):
            if node.next:
                head = recurse(node.next, node)
            else:
                head = node
            node.next = prevNode
            return head

        return recurse(head, None)




    def printList(self, head):
        print "##########################"
        curr =  head
        while curr:
            print curr.val
            curr = curr.next
        print "##########################"

    def buildList(self, arr):
        curr = head = None
        for val in arr:
            if curr:
                curr.next =  ListNode(val)
                curr = curr.next
            else:
                curr = head = ListNode(val)
        return head

if __name__ == "__main__":
    sol =  Solution()
    arr = [1,2,3,4,5]
    head = sol.buildList(arr)
    sol.printList(head)
    head = sol.reverseList(head)
    sol.printList(head)
    head = sol.reverseListRecursive(head)
    sol.printList(head)
    head = sol.reverseListRecursive(head)
    sol.printList(head)


