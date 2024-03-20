#Task1

class KeyIndex:
    def __init__(self,a):
        self.min=a[0]
        for i in a:
            if i<self.min:
                self.min=i
                
        if self.min<0:
            self.min=self.min*-1
            for i in range(0,len(a)):
                a[i]+=self.min
                
            self.max=a[0]
            for i in a:
                if i>self.max:
                    self.max=i
            self.k=[0]*(self.max+1)
            
            i=0
            while i<len(a):
                self.k[a[i]]+=1
                i+=1
            self.min=self.min*-1


        else:          
            self.max=a[0]
            for i in a:
                if i>self.max:
                    self.max=i
            self.k=[0]*(self.max+1)
            
            i=0
            while i<len(a):
                self.k[a[i]]+=1
                i+=1  
        print(self.k)



    def search(self,val):
        if self.min<0:
            val=val+self.min*-1
        if val<0 or val>len(self.k):
            print("Index Out Of Range")
            return False
        elif self.k[val]==0:
            return False
        elif self.k[val]>0:
            return True
             
        
    def sort(self):
        i=0
        j=0
        arr=[]
        if self.min<0:
            while j<len(self.k):
                
                if self.k[j]==1:
                    i=j+self.min
                    arr=arr+[i]
                    
                elif self.k[j]>1:
                    i=j+self.min
                    arr=arr+(self.k[j]*[i])
                j=j+1
        else:
            while j<len(self.k):       
                if self.k[j]==1:
                    arr=arr+[j]
                    
                elif self.k[j]>1:
                    arr=arr+(self.k[j]*[j])
                j=j+1      
        return arr
                    
                                       
# class Tester
array=[-2,3,7,8,10,-1,5,5,6] 
a=KeyIndex(array)
x=8
print(a.search(x))
print(a.sort())



#Task2

def hashTable(a):
    cons=0
    sum=0
    digcount=0
    arr=[0]*9
    vowel=["A","E","I","O","U"]
    for i in a:
        for j in i:
            if j.isalpha() and j not in vowel:
                cons+=1
            elif j.isdigit():
                digcount+=1
        sum=((cons*24)+digcount)%9
        if arr[sum]==0:
            arr[sum]=i
        else:
            while True:
                sum=(sum+1)%9
                if arr[sum]==0:
                    arr[sum]=i
                    break           
    sum=0
    cons=0
    digcount=0
    return arr
 
    
array=["ST1E89B8A32","YES1046","Q8T3","IMBATMAN22"]
print(hashTable(array))
