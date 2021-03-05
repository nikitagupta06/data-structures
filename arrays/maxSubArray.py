# Find the contiguous subarray within an array, A of length N which has the largest sum.

def maxSubArray(A):
    # max_ = 0
    # temp = 0
    
    # if max(A)<0:
    #     return max(A)

    # for i in range(len(A)):
    #     temp = temp + A[i]
    #     if temp < 0:
    #         temp = 0
    #     elif (max_ < temp):
    #         max_ = temp
    # return max_

    max_ = float('-inf')
    temp = 0
    
    for i in A:
        if temp < 0 and i > temp:
            temp = i
        else:
            temp += i
        if temp > max_:
            max_ = temp
    return max_

A = [-2,-1,-3,-4]
print(maxSubArray(A))