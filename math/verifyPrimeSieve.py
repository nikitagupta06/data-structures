# Given a number N, find all prime numbers upto N ( N included ).

import math as m

def verifyPrimeSieve(A):
    primes = [0]*(A+1)
    primes[0] = 1
    primes[1] = 1
    B=[]
    for i in range(2,int(m.sqrt(A))+1):
        if(primes[i] != 1):
            j=i
            while(i*j <= A):
                primes[i*j]=1
                j+=1
    for k in range(A+1):
        if(primes[k] == 0):
            B.append(k)
    return B

num = 163
print(verifyPrimeSieve(num))