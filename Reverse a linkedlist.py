class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

    def reverselinkedlist(self,head):
        p1,p2=None,head
        while p2!=None:
            p3=p2.next
            p2.next=p1
            p1=p2
            p2=p3

    def printlinkedlist(self,head):
        while head!=None:
            print(head.data)
            head=head.next
        print('end of order')
        
        


node1 = Node(2)
node2= Node(3)
node3 = Node(4)
node4 = Node(5)


node1.next =node2
node2.next=node3
node3.next=node4

node1.printlinkedlist(node1)

node1.reverselinkedlist(node1)



node1.printlinkedlist(node4)



# a more 'pro' version of code:





class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

    def reverselinkedlist(self):
        p1,p2=None,self
        while p2!=None:
            p3=p2.next
            p2.next=p1
            p1=p2
            p2=p3

    def printlinkedlist(self):
        while self!=None:
            print(self.data)
            self=self.next
        print('end of order')
        
        


node1 = Node(2)
node2= Node(3)
node3 = Node(4)
node4 = Node(5)


node1.next =node2
node2.next=node3
node3.next=node4

node1.printlinkedlist()

node1.reverselinkedlist()



node4.printlinkedlist()




