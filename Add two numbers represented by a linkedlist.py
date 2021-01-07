class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        dummyhead = ListNode(0)
        current = dummyhead
        sum=0
        carry=0
        p,q=l1,l2
        while (p!= None or q!= None):
            x= p.val if p!=None else 0
            y = q.val if q!= None else 0
            sum = x+y+carry
            carry = sum//10
            current.next = ListNode(sum%10)
            current = current.next
            if (p!=None):
                p=p.next
            if (q!=None):
                q=q.next
        if carry >0:
            current.next = ListNode(carry)
        return dummyhead.next
