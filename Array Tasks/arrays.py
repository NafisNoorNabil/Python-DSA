#task1
def shiftLeft(source,k):
    i=0
    while i<len(source)-k:
        source[i]=source[i+k]
        i+=1
    i=len(source)-k
    while i<len(source):
        source[i]=0
        i+=1

    print(source)
        
source=[10,20,30,40,50,60]
shiftLeft(source,3)


#task2
def rotateLeft(source,k):
    i=0
    temp=[0]*k
    while i<k:
        temp[i]=source[i]
        i+=1
    i=0
    while i<len(source)-k:
        source[i]=source[i+k]
        i+=1
    i=len(source)-k
    j=0
    while i<len(source):
        source[i]=temp[j]
        i+=1
        j+=1
    print(source)
source=[10,20,30,40,50,60]
rotateLeft(source,3)



#task3
def remove(source,size,idx):
    if size==len(source):
        print("No Space in Array")
        return False
    if idx<0 or idx>=size:
        print("Invalid Index")
        return False
    i=idx
    while i<size-1:
        source[i]=source[i+1]
        i+=1
    source[size-1]=0
    print(source)


source=[10,20,30,40,50,0,0]
remove(source,5,2)


#task4
def removeAll(source,size,element):
    new=[0]*len(source)
    i=0
    while i<=size-1:
        if source[i]==element:
            source[i]=0
        i+=1
    i=0
    j=0
    while i<=size-1:
        if source[i]!=0:
            new[j]=source[i]
            j+=1
        i+=1
    print(new)

source=[10,2,30,2,50,2,2,0,0]
removeAll(source,7,2)


#task5
def splitArray(source):
    sum1=0
    sum2=0
    for i in source:
        sum1=sum1+i
    i=0
    
    while i <len(source):
        sum1=sum1-source[i]
        sum2=sum2+ source[i]
        i+=1
        
        if sum1==sum2:
            return True
        
    return False
        

source=[1,1,1,2,1]
print(splitArray(source))



#task6
def arrSeries(n):
    arr=[0]*(n*n)
    i=0
    for j in range(0,n):
        for k in range(0,n):
            arr[i]=k+1
            i+=1
    arr.reverse()
    i=0
    j=0
    temp=n
    for i in range(0,n):
        for j in range(0,temp-1):
            arr[j]=0
        temp-=1

    print(arr)
arrSeries(int(input("Input N:")))


#task7
def MaxBunch(s):
    i=0
    count=1
    new=[]
    while i<len(s)-1:
        if s[i]==s[i+1]:
            count+=1    
        else:
            new.append(count)
            count=1
        i+=1
        if i==len(s)-1:
            new.append(count)
    max=0
    for i in new:
        if i>max:
            max=i
    print(max)
        
    
source=[1,2,2,3,4,4,4] 
MaxBunch(source)



#task8
def repetition(x):
    i=0
    new=[]
    while i<len(source):
        if source[i] not in new:
            new.append(source[i])
        i+=1
    count1=0
    i=0
    j=0
    rep=[]
    while i<len(new):
        while j<len(source):
            if new[i]==source[j]:
                count1+=1
            j+=1
        rep.append(count1)
        i+=1
        count1=0
        j=0
    i=0
    j=1
    while i<len(rep):
        while j<len(rep):
            if rep[i]>1 and rep[i]==rep[j]:
                return True
            j+=1
        i+=1
        j=i+1
    return False

source=[4,5,6,6,4,3,6,4]
print(repetition(source))



#task9
def Palindrome(s,start,size):
    i=start
    j=(start+size-1)%len(s)
    count=0

    for k in range(0,size//2): 
        if s[i]!=s[j]:
            return False
        i=(i+1)%len(s)
        j-=1
        if j<0:
            j=len(s)-1 
    return True           

    
source=[10,20,0,0,0,10,20,30]
print(Palindrome(source,5,5))


#task10
def intersection(c1,start_1,size_1,c2,start_2,size_2):
    new=[]
    i=0
    j=0
    index1=start_1
    index2=start_2

    while i<size_1:
        while j<size_2:
            if c1[index1]==c2[index2]:
                new.append(c1[index1])
            j+=1
            index2=(index2+1)%len(c2)

        i+=1
        j=0
        index1=(index1+1)%len(c1)
        index2=start_2

    print(new)
        
circ1=[40,50,0,0,0,10,20,30]
circ2=[10,20,5,0,0,0,0,0,5,40,15,25]
intersection(circ1,5,5,circ2,8,7)