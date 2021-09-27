def moveAllToOneSide(arr):
    w = 0
    for i in range(len(arr)):
        if(arr[i]>=0 and i<len(arr)-w):
            arr.append(arr[i])
            del arr[i]
            i-=1
            w+=1
    return arr

#drivers code
A = [-12,11,-13,-5,6,-7,5,-3,-6]
print(A)
print(moveAllToOneSide(A))