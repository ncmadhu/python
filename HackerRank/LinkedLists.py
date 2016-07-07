class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class Solution:
    def display(self,head):
        current = head
        while current:
            print current.data,
            current = current.next
            
    def insert(self,head,data): 
    #Complete this method
        if head:
            current = head
            while current.next:
                current = current.next
            node = Node(data)
            current.next = node
        else:
            node = Node(data)
            head =  node
        return head
        
mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
mylist.display(head);