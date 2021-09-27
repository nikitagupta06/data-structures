# Given an array A of size N. You need to find the sum of Maximum and Minimum element in the given array.


def sumOfMaxMin(A):
    max = A[0]
    min = A[0]
    for i in range(len(A)):
        if(A[i]>=max):
            max = A[i]
        if(A[i]<=min):
            min = A[i]
    return (max + min)

A = [1, 3, 4, 1]
print(sumOfMaxMin(A))