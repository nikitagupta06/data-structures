# rotate A[] of size n by B elements.

def rotateArray(A, B):
    arr = []
    if(B>len(A)):
        B = B%len(A)
    for i in range(len(A)):
        arr.append(A[i+(B-len(A))])
    return arr

A = [1,2,3,4,5,6,7]
print(rotateArray(A,2))