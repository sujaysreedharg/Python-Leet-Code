# creating a class called node
class Node:
    # function to create a node
    def __init__(self,data):
        self.data = data
        self.next = None
class linkedlist:
    def __init__(self):
        self.head=None
    def printlist(self):
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next
if __name__=='__main__':
    llist= linkedlist()
    llist.head=Node(1)
    second= Node(2)
    third=Node(3)
    llist.head.next= second
    second.next=third
    llist.printlist()
