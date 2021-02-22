
# Given a non-negative number represented as an array of digits,

# add 1 to the number ( increment the number represented by the digits ).

# The digits are stored such that the most significant digit is at the head of the list.

# Example:

# If the vector has [1, 2, 3]

# the returned vector should be [1, 2, 4]

# as 123 + 1 = 124.


# @param A : list of integers
# @return a list of integers
def addOne(A):
    for i in range(len(A)-1,-1,-1):
        if(A[i]==9):
            A[i] = 0
        else:
            A[i] += 1
            while True:
                if A[0] == 0:
                    del A[0]
                else:
                    return A
            return A
    A = [1] + A
    return A

A=[9,9,9,9]
print(addOne(A))