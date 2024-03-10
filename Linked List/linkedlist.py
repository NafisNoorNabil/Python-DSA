#Task 1 (i)
class Node:
    def __init__ (self,value,next):
        self.value=value
        self.next=next
        
#Task1 (ii)

class MyList:
#Task2(1a)
    def __init__(self,a=None):  
        self.head=None
        
        
            
#Task 2 (1b)
        if isinstance(a ,list): 
            self.head=None
            tail=None
            for i in a:
                n=Node(i,None)
                if self.head==None:
                    self.head=n
                    tail=n
                else:
                    tail.next=n
                    tail=n
                    
                    
#Task 2(1c)           
        elif isinstance(a,MyList):
            self.head=None
            tail=None
            n=a.head
            while n!=None:
                newNode=Node(n.value,None)
                if self.head==None:
                    self.head=newNode
                    tail=newNode
                else:
                    tail.next=newNode
                    tail=newNode
                n=n.next
                
                
# #Task 2 (2)
    def showList(self):
        n=self.head
        if self.head==None:
            print("Empty List")
        else:
            while n!=None:
                print(n.value)
                n=n.next

                
#Task2 (3)
    def isEmpty(self):
        if self.head==None:
            return True
        else:
            return False

        
#Task2 (4)
    def clear(self):
        if self.head != None:
            self.head=None
 
            
#Task2 (5)
    def insert(self,newElement):
        n=self.head
        newNode = Node(newElement,None)
        if self.head==None:
            self.head=newNode
        else:
            while n!=None:
                if n.value==newElement:
                    return "newElement Already Exists"
                
                n=n.next
            temp=self.head
            while temp.next!=None:
                temp=temp.next
            temp.next=newNode
        return self.head
            

    

# #Task2 (6)
    def insertidx (self,newElement,index):
        newNode = Node(newElement,None)
        n=self.head

        if self.head==None:
            self.head=newNode
        else:
            while n!=None:
                if n.value==newElement:
                    return "newElement Already Exists"
                n=n.next
            count=1
            n=self.head
            while n!=None and count<index:
                n=n.next
                count+=1
            newNode.next=n.next
            n.next=newNode
        return self.head
    
    
                        
#Task2 (7)  
    def remove(self,deleteKey):
        prev=self.head
        n=self.head.next
        if self.head==None:
            print("Empty List")
        else:
            while n!=None:
                if n.value==deleteKey:
                    prev.next=n.next
                    n=None
                    return
                n=n.next
                prev=prev.next
                    
                 
   
#Task 3 (1)
    def Even(self):
        n=self.head
        self.head2=None
        tail=None
        while n != None:
            if n.value%2==0:
                newNode=Node(n.value,None)
                if self.head2==None:
                    self.head2=newNode
                    tail=newNode
                else:
                    tail.next=newNode
                    tail=newNode 
            n=n.next
        n=self.head2
        while n != None:
            print(n.value)
            n=n.next
            
        
            
             
#Task 3 (2)
    def Elementcheck(self,element):
        n=self.head
        while n !=None:
            if n.value==element:
                return True
            n=n.next
        return False
            
        
      
#Task 3 (3)   
    def reverseList(self):
        n=self.head
        nxt=self.head.next
        previous=None
        while n!=None:
            nxt=n.next
            n.next=previous
            previous=n
            n=nxt
        self.head=previous
        return self.head


# #Task 3 (4)
    def Sort(self):
        node1=self.head
        node2=self.head
        while node1!=None:
            while node2!=None:
                if node1.value<node2.value:
                    temp=node2.value
                    node2.value=node1.value
                    node1.value=temp
                node2=node2.next
            if node2==None:
                node2=self.head
            node1=node1.next
 

#Task 3 (5)
    def Sum(self):
        n=self.head
        if self.head==None:
            return 0
        else:
            sum=0
            while n != None:
                sum=sum+n.value
                n=n.next
            print(sum)



lst = MyList()
lst1 = MyList([1, 6, 5, 9])
lst2 = MyList(lst1)

print(lst)
print(lst1)
print(lst2)
lst1.showList()

#check if a list is empty
print("Empty Check:")
print(lst1.isEmpty())

#clear list check
print("Clear list check:")
lst2.clear()
print(lst2)
lst2.showList()

#insert element at the end check
print("insert element at the end check:")
lst2=lst1.insert(2)
lst1.showList()
print(lst2)

#intert element at a given index check
print("intert element at a given index check:")
lst2=lst1.insertidx(4,4)
lst1.showList()
print(lst2)

#remove Check
print("Remove Check:")
lst1.remove(6)
print(lst1)
lst1.showList()

#Even Check
print("Even Check:")
lst1.Even()

#Element check
print("Element check: ")
print(lst1.Elementcheck(5))
print(lst1.Elementcheck(0))

#sum check
print("Sum Check:")
lst1.Sum()

print("Sort Check: ")
lst1.Sort()
lst1.showList()
print(lst1)

print("Reverse Check: ")
lst1.reverseList()
print(lst1)
lst1.showList()


        