def removeDupsSortedArray(A):
    leng = len(A)
    i=1
    while leng > 0 and i < leng :
        if(A[i] == A[i-1]):
            del A[i]
            leng-=1
            i-=1
        i+=1
    return A

A = [0,0,1,1,1,2,3,3,4]
print(removeDupsSortedArray(A))