


def insertion_sort(A):
  for i in range(0,len(A)):
    for j in range(i-1,-1,-1):
      if A[j]<A[j+1]:
        temp = A[j]
        A[j]=A[j+1]
        A[j+1]=temp
      else:
        break
y=open("D:\input3.txt","r")
out=open("D:\output3.txt","w")
x=y.readlines()
N=int(x.pop(0))
arr=[0]*N