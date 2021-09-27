# You are in an infinite 2D grid where you can move in any of the 8 directions

# You are given a sequence of points and the order in which you need to cover the points.. 
# Give the minimum number of steps in which you can achieve it. You start from the first point.

# Input Format
# Given two integer arrays A and B, where A[i] is x coordinate and B[i] is y coordinate of ith point respectively.

# Output Format
# Return an Integer, i.e minimum number of steps.



def minStepsInfiniteGrid(A,B):
    steps = 0
    for i in range(len(A)-1):
        n = abs(A[i]-A[i+1])
        m = abs(B[i]-B[i+1])
        steps += max(n,m)    
    return steps

A = [ 4, 8, -7, -5, -13, 9, -7, 8 ]
B = [ 4, -15, -10, -3, -13, 12, 8, -8 ]
print(MinStepsInfiniteGrid(A,B))