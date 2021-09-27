#  Given a number N >= 0, find its representation in binary.

def binaryRepresentation(A):
    stri = ""
    if(A == 0):
        return 0
    while(A>0):
        rem = A%2
        stri += str(rem)
        A=A//2
    return stri[::-1]


print(binaryRepresentation(125))