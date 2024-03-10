#right shifting an array by k places

def rightShift(source,k):

    i=len(source)-k #pointer at the last index of source
    temp=[0]*k
    j=0
    while i<=len(source)-1:
        temp[j]=source[i]
        i+=1
        j+=1

    i=len(source)-1
    while(i>=k):

        source[i]=source[i-k]  #shifting elements k places to the right

        i=i-1

    i=0
    while(i<k):
        source[i]=temp[i]
        i+=1





a=[10,20,30,40,50,60]

rightShift(a,3)

print(a)