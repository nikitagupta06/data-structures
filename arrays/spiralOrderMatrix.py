# Given a matrix of m * n elements (m rows, n columns), return all elements of the matrix in spiral order.

# Example:

# Given the following matrix:

# [
#     [ 1, 2, 3 ],
#     [ 4, 5, 6 ],
#     [ 7, 8, 9 ]
# ]
# You should return

# [1, 2, 3, 6, 9, 8, 7, 4, 5]


def spiralOrderMatrix(A):
    i=0
    j=0
    imin=0
    imax=len(A)
    jmin=-1
    jmax=len(A[0])
    result = []

    total = imax*jmax
    count = 0

    while (imin < imax and jmin < jmax):
        if count==total:
            break
        for j in range(jmin+1,jmax):
            result.append(A[i][j])
            count+=1
        jmax-=1
        if count==total:
            break
        for i in range(imin+1,imax):
            result.append(A[i][j])
            count+=1
        imax-=1
        if count==total:
            break
        for j in range(jmax-1,jmin,-1):
            result.append(A[i][j])
            count+=1
        jmin+=1
        if count==total:
            break
        for i in range(imax-1,imin,-1):
            result.append(A[i][j])
            count+=1
        imin+=1
    return result

#driver code
A =[[1, 2, 3, 4],
    [10, 11, 12, 5],
    [9, 8, 7, 6]]
print(spiralOrderMatrix(A))
