# Given an array of integers, A of length N, find out the maximum sum sub-array of non negative numbers from A.

# The sub-array should be contiguous i.e., a sub-array created by choosing the second and fourth element and skipping the third element is invalid.

# Maximum sub-array is defined in terms of the sum of the elements in the sub-array.

# Find and return the required subarray.

# NOTE:

# If there is a tie, then compare with segment's length and return segment which has maximum length.
# If there is still a tie, then return the segment with minimum starting index.



def maxNonNegativeSubArray(A):
    sum = -1
    st=0
    end=0
    smax=0
    stmax=0
    emax=0
    A = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    for i in range(len(A)):
        if(A[i]>=0):
            if(sum == -1):
                st = i
                sum = 0
            sum+=A[i]
        else:
            if(sum == -1 and A[i]<0):
                i+=1
            else:
                end = i
                if(sum > smax):
                    smax = sum
                    stmax = st
                    emax = end
                elif (sum == smax and st > stmax):
                    stmax = st
                    emax = end
                sum = -1
                st = 0
                end =0

    return A[stmax:emax]

A = [-1, 5, 0, -5, -7, 0, 0, 3, 2]
print(maxNonNegativeSubArray(A))