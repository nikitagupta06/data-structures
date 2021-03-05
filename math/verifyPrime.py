# Given a number N, verify if N is prime or not.

# Return 1 if N is prime, else return 0.

import math as m

def verifyPrime(A):
    if A == 1:
        return 0
    for i in range(2,int(m.sqrt(A)+1)):
        if(A%i==0):
            return 0
    return 1
num = 1
print(verifyPrime(num))