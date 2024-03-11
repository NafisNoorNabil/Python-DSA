class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Queue:
    head=None
    tail=None

    def enqueue(self, element):
        n=Node(element)
        if self.head==None:
            self.head=n
            self.tail=n
        else:
            self.tail.next=n
            self.tail=n

    def dequeue(self):
        temp=self.head
        self.head=self.head.next
        print(temp.data)
        temp.data=None
        temp.next=None

    def peek(self):
        return(self.head.data)

que=Queue()
que.enqueue(1)
que.enqueue(2)
que.enqueue(3)
que.enqueue(4)
que.enqueue(5)
print("Top data:",que.peek())
que.dequeue()
print("Top data:",que.peek())
