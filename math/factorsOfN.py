# Given a number N, find all factors of N.

import math as m

def factorsOfN(N):
    A = []
    sq = m.sqrt(N)
    for i in range(1,int(sq)+1):
        if(N%i==0):
            A.append(i)
            if(i != sq):
                A.append(int(N/i))
    A.sort()
    return A

N = 36
print(factorsOfN(N))