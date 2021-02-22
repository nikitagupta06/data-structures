# Given an array of integers, A of length N, find out the maximum sum sub-array of non negative numbers from A.

# The sub-array should be contiguous i.e., a sub-array created by choosing the second and fourth element and skipping the third element is invalid.

# Maximum sub-array is defined in terms of the sum of the elements in the sub-array.

# Find and return the required subarray.

# NOTE:

# If there is a tie, then compare with segment's length and return segment which has maximum length.
# If there is still a tie, then return the segment with minimum starting index.



def maxNonNegativeSubArray(A):
    st = 0
    end = 0
    sum = -1 
    stmax = 0
    emax = 0
    smax = 0
    i = 0
    n = len(A)

    while(i<n and A[i]<0):
        i+=1
    while(i<n):
        if(sum == -1):
            sum = 0
            st = i
        if(A[i] < 0):
            end = i
            if(sum > smax):
                smax = sum
                stmax = st
                emax = end
            elif(sum == smax):
                if ((end-st) > (emax-stmax)):
                    stmax = st
                    emax = end
            st = 0
            end = 0
            sum = -1
        else:
            sum += A[i]
        i+=1
    if(A[i-1] >= 0):
        end = i
    if(sum > smax):
        smax = sum
        stmax = st
        emax = end
    elif(sum == smax):
        if((i-st) > (emax-stmax)):
            stmax = st
            emax = end

    return A[stmax:emax]

A = [-1, 5, 0, -5, -7, 0, 0, 3, 2]
print(MaxNonNegativeSubArray(A))