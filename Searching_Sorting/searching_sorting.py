
#Task 1

def selectionSort(a,i,j):
 
    l=len(a)
    if i == l and j==l:
      return -1


    if i < l-1:
      min=i

      while j < l:
        if a[j] < a[min]:
          min = j
        
        j=j+1

      if min != i:
        temp=a[i]
        a[i]=a[min]
        a[min]=temp

      selectionSort(a,i+1,i+2)

array=[2,6,-1,1,3,5,8,9,0]
i=0
j=i+1
selectionSort(array,i,j)
print(array)


#Task 2

def insertionSort(a,i):
    
    l=len(a)

    if i == l:
      return -1

    for j in range(i-1,-1,-1):
      
        if a[j]>a[j+1]:
            temp = a[j]
            a[j]=a[j+1]
            a[j+1]=temp
          
        else:
          break
    
    insertionSort(a,i+1)

array=[2,6,-1,1,3,5,8,9,0]
i=0
insertionSort(array,i)
print(array)



#Task3
class Node:
    def __init__ (self,value,next):
        self.value=value
        self.next=next 
        
class MyList:
    def __init__(self,a):  
        self.head=None
        
        
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
                   
    def bubbleSort(self):
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
 
         
    def showList(self):
        n=self.head
        if self.head==None:
            print("Empty List")
        else:
            while n!=None:
                print(n.value,end=" ")
                n=n.next



#Task 4
    def selectionSort(self):    
        node1=self.head
        node2=self.head
        
        while node1!=None:
            min=node1.value
            
            while node2!=None:
                if node2.value<min:
                    min=node2.value
                node2=node2.next
                
            n=self.head    
            while n!=None:
                if n.value==min:
                    break
                n=n.next
                    
            temp=node1.value
            node1.value=min
            n.value=temp
            node2=node1.next
            node1=node1.next
                        

lst = MyList([2,6,-1,1,3,5,8,9,0])
#need to comment the lst.bubbleSort() or lst.selectionSort() to check if both of them works
lst.bubbleSort()
lst.showList()
lst.selectionSort()



#Task5
class DoublyNode:

    def __init__(self,value,next,prev):
        self.value = value
        self.next = next
        self.prev = prev
        
class DoublyList:
    def __init__(self,a):
        self.head=None
         
        if isinstance(a,list):
            self.head = None
            tail = None
            
            for i in a:
                n=DoublyNode(i,None,None)
                if self.head==None:
                    self.head=n
                    tail=n 
                else:
                    tail.next=n
                    n.prev=tail
                    tail=n
      
    def showList(self):
        n=self.head
        if self.head==None:
            print("Empty List")
        else:
            while n!=None:
                print(n.value,end=" ")
                n=n.next

    def insertionSort(self):
        n=self.head

        while n!=None:
            j=n.prev
            while j!=None:
                if j.value>j.next.value:
                    temp=j.value
                    j.value=j.next.value
                    j.next.value=temp
                j=j.prev
            n=n.next
                     
lst = DoublyList([2,6,-1,1,3,5,8,9,0])
print(" \n Doubly linked insertion sort check: ")
lst.insertionSort()
lst.showList()




#Task6
def binary_search(A,L,R,val):
    

    if L<=R:
      M = (L+R)//2

      if val == A[M]:
        return M

      elif val > A[M]:
          return binary_search(A,M+1,R,val)
      else:
          return binary_search(A,L,M-1,val)
       
A=[2,4,7,9,12,14,15]
L=0
R=len(A)-1
print(" \nBinary Search:",binary_search(A,L,R,9))




#Task 7
store={}
def fibonacci(num):
    if num in store:
        return store[num]
    if num == 0:
        return 1

    elif num == 1:
        return 1
    
    else:
        x=(fibonacci(num-1)+fibonacci(num-2))
    store[num]=x
    return x

num=13
x=fibonacci(num)
print("Fibonacci Sequence: ")
for num in range(0,num):
    print(fibonacci(num))
    




