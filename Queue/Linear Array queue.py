class Queue:
    li=[]
    front=0
    pos=-1

    def enqueue(self,element):
        self.li.append(element)
        self.pos+=1

    def dequeue(self):
        temp=self.li[self.front]
        self.li=self.li[self.front+1:]
        self.pos-=1
        return temp

    def peek(self):
        return (self.li[self.front])



que=Queue()
que.enqueue(1)
que.enqueue(2)
que.enqueue(3)
que.enqueue(4)
que.enqueue(5)
que.dequeue()
print(que.peek())