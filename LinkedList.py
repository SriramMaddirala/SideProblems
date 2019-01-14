class Node:
    def __init__(self,data= None,next= None,):
        self.data = data
        self.next = next
class LinkedList:
    def __init__(self):
        self.head= None
    def search(self,x):
        current = self.head
        while(current!=None):
            if(current.data==x):
                return True
            else:
                current = current.next
        return False
    def insert(self,x):
        x.next = self.head
        self.head = x
    def reverse(self):
        tail = self.head
        if(tail.next==None):
            return self.head
        while(tail.next!=None):
            tail = tail.next
        temp = tail
        self.reverselist(tail)
        self.head = temp
    def reverselist(self,tail):
        head = self.head
        while(head.next != tail):
            if(tail == head):
                tail.next = None
                return
            head = head.next
        tail.next = head
        if(tail != self.head):
            tail = head
            self.reverselist(tail)
    def delete(self):
        self.head = self.head.next
a = LinkedList()
b = Node("Hello")
c = Node("Late")
d = Node("Not")
e = Node("Nope")
f = Node("Dope")
a.insert(b)
a.insert(c)
a.insert(d)
a.insert(e)
a.insert(f)
print(a.search("Not"))
a.reverse()
a.delete()
a.delete()
a.delete()
a.delete()
a.delete()