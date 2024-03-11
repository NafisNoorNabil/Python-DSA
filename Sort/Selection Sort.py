
def selection_sort(A):

  for i in range(len(A)-1,-1,-1):


    max_idx = i


    for j in range(0,i):

      if(A[j]>A[max_idx]):

        max_idx = j

    temp = A[max_idx]
    A[max_idx]=A[i]

    A[i]=temp
x=[5,4,3,7,8,1]
selection_sort(x)
print(x)



