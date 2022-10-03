###IMPLEMENTATION OF DOUBLE LINKED LIST##
class Node:
    def __init__(self,dataval=None):
        self.dataval=dataval
        self.next=None
        self.prev=None
class DoubleList:##List Operations
    def __init__(self):
        self.head=None
    def display(self):##Display the list
        curr=self.head
        while curr is not None:
            print(curr.dataval)
            curr=curr.next
    def pushFront(self,item):
        NewNode=Node(item)
        NewNode.next=self.head
        NewNode.prev=None
        self.head=NewNode
        return
    def pushLast(self,item):
        NewNode=Node(item)
        curr=self.head
        while curr.next is not None:
            curr=curr.next
        curr.next=NewNode
        NewNode.prev=curr
        NewNode.next=None
        return
    def pushMiddle(self,item,pos):
        NewNode=Node(item)
        curr=self.head
        count=1
        while count<pos-1:
            curr=curr.next
            count=count+1
        NewNode.next = curr.next.next
        curr.next=NewNode
        NewNode.prev=curr
        return
    def deleteFront(self):
        curr=self.head
        temp=curr.next
        temp.prev=None
        self.head=temp
        curr=None
        return
    def deleteLast(self):
        curr=self.head
        while curr.next.next is not None:
            curr=curr.next
        temp=curr.next
        curr.next=None
        temp=None
        return
    def deleteMiddle(self,pos):
        curr=self.head
        count=1
        while count<pos-1:
            curr=curr.next
            count=count+1
        temp=curr.next
        curr.next=curr.next.next
        temp.prev=curr.next.prev
        temp=None
        return
list1=DoubleList()
list1.head=Node("Mon")
e2=Node("Tue")
e3=Node("Wed")
list1.head.prev=None
list1.head.next=e2
e2.prev=list1.head.next
e2.next=e3
e3.prev=e2.next
list1.display()
print()
list1.pushFront("Front")
list1.display()
print()
list1.pushLast("Last")
list1.display()
print()
list1.pushMiddle("Three",3)
list1.display()
print()
list1.deleteFront()
list1.display()
print()
list1.deleteLast()
list1.display()
print()
list1.deleteMiddle(2)
list1.display()
print()
