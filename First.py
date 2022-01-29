from locale import currency
from operator import ne


class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class linkedlist:
    def __init__(self):
        self.head=None
    def ghumo(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp=temp.next
    def modo(self):
        temp=self.head
        prev=self.head
        curr=self.head
        n_e=self.head
        while(curr.next):
            #curr=prev.next
            n_e=curr.next
            curr.next=prev
            prev=curr
            curr=n_e
        curr.next=prev
        self.head=curr
        temp.next=None



if __name__=='__main__':
    llist=linkedlist()

    llist.head= node(1)
    a=node(2)
    b=node(3)
    c=node(4)
    d=node(5)
    e=node(6)

    #linking nodes

    llist.head.next=a
    a.next=b
    b.next=c
    c.next=d
    d.next=e
    llist.modo()
    llist.ghumo()
        

