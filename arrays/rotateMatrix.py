# You are given an n x n 2D matrix representing an image.

# Rotate the image by 90 degrees (clockwise).

# You need to do this in place.

# Note that if you end up using an additional array, you will only receive partial score.


def rotateMatrix(A):
    top_index = 0
    right_index = 0
    left_index = len(A)-1
    bottom_index = len(A)-1
    rows = 0
    col = len(A)-1
    count = len(A)//2

    while (rows != col and col > 0 and rows < (len(A)-1)) or count>0:
        for i in range(rows+1, col+1):
            A[rows][top_index], A[right_index][col] = A[right_index][col], A[rows][top_index]
            A[rows][top_index], A[bottom_index][rows] = A[bottom_index][rows], A[rows][top_index]
            A[col][left_index], A[bottom_index][rows] = A[bottom_index][rows], A[col][left_index]
            top_index += 1
            right_index += 1
            left_index -= 1
            bottom_index -= 1
        rows += 1
        col -= 1
        top_index = rows
        right_index = rows
        left_index = col
        bottom_index = col
        count -= 1
    return A

    # # Transpose
    # for i in range(len(A)):
    #     for j in range(i,len(A)):         
    #         A[i][j], A[j][i] = A[j][i], A[i][j]
    # # Reverse 
    # for i in range(len(A)):
    #     A[i].reverse()
    # return A

A=[
  [31, 32, 228, 333],
  [79, 197, 241, 246],
  [77, 84, 126, 337],
  [110, 291, 356, 371]
]
for i in A:
    print(i)
z=rotateMatrix(A)
print("---------------")
for i in z:
    print(i)