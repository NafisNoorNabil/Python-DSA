

#Task1

class Stack:
    stack=[]
    pointer=-1

    def Push(self,value):
        self.stack.append(value)
        self.pointer+=1

    def Peek(self):
        return(self.stack[self.pointer])
            
    def Pop(self):
        value=self.stack[self.pointer]
        self.stack=self.stack[:-1]
        self.pointer-=1
        return value
    
    def Parenthesis(self,a):
        Open=["(","{","["]
        Close=[")","}","]"]
        count=0
    
        for i in a:
            count+=1
       
            if i in Open:
                self.Push(i)
                
            elif i in Close and len(self.stack)==0:
                print(a)
                print("Error at character #",count,"'"+i+"'","- not opened")
                return
            elif i in Close:
                if self.Peek()==("(") and i== (")") :
                    self.Pop()
                elif self.Peek()==("{") and i==("}"):
                    self.Pop()
                elif self.Peek()==("[") and i==("]"): 
                    self.Pop()
                else:
                    print(a)
                    print("Error at character# ",a.index(self.Peek())+1,"'"+self.Peek()+"'","not closed")
                    return
                
        if len(self.stack)>0:
            print(a)
            print("Error at character #",a.index(self.Peek())+1,"'"+self.Peek()+"'","- not closed.")
            return
        else:
            print(a)
            print("This expression is correct")
            return
stack1=Stack()
stack1.Parenthesis("1+2*[3*3+{4–5(6(7/8/9)+10)–11+(12*8)]+14")




#Task2
class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
        
class stackList:
    head=None
    
    def Push(self,data):
        if self.head is None:
            self.head=Node(data)
        else:
            n=Node(data)
            n.next=self.head
            self.head=n
            
    def Peek(self):
        return self.head.value
    
    def Pop(self):
        temp=self.head
        self.head=self.head.next
        temp.value=None
        temp.next=None
        
    def Parenthesis(self,a):
        Open=["(","{","["]
        Close=[")","}","]"]
        count=0
        
        for i in a:
            count+=1
            
            if i in Open:
                self.Push(i)
                
            elif i in Close and self.head==None:
                print(a)
                print("Error at character #",count,"'"+i+"'","- not opened")
                return
            elif i in Close:
                if self.Peek()==("(") and i== (")") :
                    self.Pop()
                elif self.Peek()==("{") and i==("}"):
                    self.Pop()
                elif self.Peek()==("[") and i==("]"): 
                    self.Pop()
                else:
                    print(a)
                    print("Error at character # ",a.index(self.Peek())+1,"'"+self.Peek()+"'","not closed")
                    return
                
        if self.head!=None:
            print(a)
            print("Error at character #",a.index(self.Peek())+1,"'"+self.Peek()+"'","- not closed.")
            return
        else:
            print(a)
            print("This expression is correct")
            return


stack=stackList()
stack.Parenthesis("1+2]*[3*3+{4–5(6(7/8/9)+10)–11+(12*8)]+14")


