
#Task1 (i)
class Node:

    def __init__(self,value,next,prev):
        self.value = value
        self.next = next
        self.prev = prev
        
#Task 1 (ii)
class DoublyList:
    def __init__(self,a):
        self.head=None
        
        
#Task2 (1a)
        if isinstance(a,list):
            head=Node(None,None,None)
            self.head=head
            tail=self.head
            for i in a:
                newNode=Node(i,None,None)
                if self.head==None:
                    self.head.next=newNode
                    tail=newNode
                else:
                    tail.next=newNode
                    newNode.prev=tail
                    tail=newNode
                tail.next=head
                head.prev=tail
                
                
#Task 2 (2)
    def showList(self):
        n=self.head.next
        if self.head.next==None:
            print("Empty list")
        else:
            while n!=self.head:
                print(n.value)
                n=n.next
                    
                
#Task 3            
    def insert(self,newElement):
        n=self.head.next
        newNode = Node(newElement,None,None)
        if self.head.next==None:
            self.head.next=newNode
        else:
            while n!=self.head:
                if n.value==newElement:
                    return "newElement Already Exists"
                n=n.next
            temp=self.head.next
            while temp.next!=self.head:
                temp=temp.next
            temp.next=newNode
            newNode.next=self.head
            newNode.prev=temp
            self.head.prev=newNode
            
            
#Task 4
    def insertindex(self,newElement,index):
        n=self.head.next
        newNode = Node(newElement,None,None)
        if self.head.next==None:
            self.head.next=newNode
        else:
            while n!=self.head:
                if n.value==newElement:
                    return "newElement Already Exists"
                n=n.next
            count=1
            temp=self.head.next
            while temp.next!=self.head and count<index:
                temp=temp.next
                count+=1
            q=temp.next
            newNode.next=temp.next
            newNode.prev=temp
            temp.next=newNode
            q.prev=newNode

            


#Task 5
    def remove(self,index):
        if index<0:
            print("invalid index")
            return
        n=self.head.next
        if self.head==None:
            print("Empty List")
        else:
            count=0
            while n!=self.head:
                p=n.prev
                q=n.next
                if count==index:
                    p.next=q
                    q.prev=p
                    n.next=None
                    n.prev=None  
                    return
                count+=1
                n=n.next
 
        
        
#Task6            
    def removeKey(self,deleteKey):
        n=self.head.next
        if self.head==None:
            print("Empty List")
            
        else:
            while n!=self.head:
                p=n.prev
                q=n.next
                if n.value==deleteKey:
                    p.next=q
                    q.prev=p
                    n.next=None
                    n.prev=None
                    return
                n=n.next



            
lst = DoublyList([1, 6, 5, 9])
lst.showList()
print(lst)

#insertcheck
print("Insert Check: ")
lst.insert(7)
lst.showList()

#insert at an index check
print("insert at an index check: ")
lst.insertindex(4,1)
lst.showList()

#remove node check
print("Remove Node Check")
lst.remove(2)
lst.showList()


#Remove key check
print("Remove Key Check: ")
lst.removeKey(9)
lst.showList()








 