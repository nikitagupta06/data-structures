# You are given an array of N integers, A1, A2 ,…, AN. Return maximum value of f(i, j) for all 1 ≤ i, j ≤ N.
# f(i, j) is defined as |A[i] - A[j]| + |i - j|, where |x| denotes absolute value of x.

def maxAbsDiff(A):
    # ab = 0
    # for i in range(len(A)):
    #     for j in range(i, len(A)):
    #         ab = max(abs(A[i]-A[j])+abs(i-j),ab)
    # return ab

    a=[]
    b=[]
    for i in range(len(A)):
        a.append(A[i]+i)
        b.append(A[i]-i)
    return max(max(a)-min(a),max(b)-min(b))

A = [-1,-1,-1,-1]
print(maxAbsDiff(A))