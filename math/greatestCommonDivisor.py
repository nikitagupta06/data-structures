# Given 2 non negative integers m and n, find gcd(m, n)

# GCD of 2 integers m and n is defined as the greatest integer g such that g is a divisor of both m and n.
# Both m and n fit in a 32 bit signed integer.

def greatestCommonDivisor(A, B):
    L = min(A, B)
    if(L == 0):
        return max(A,B)
    elif(A%L == 0 and B%L == 0):
        return L
    else:
        for i in range(L//2,1,-1):
            if(A%i==0 and B%i==0):
                return i
        return 1
    

print(greatestCommonDivisor(10,0))