# Given a positive integer A, return an array of strings with all the integers from 1 to N.
# But for multiples of 3 the array should have “Fizz” instead of the number.
# For the multiples of 5, the array should have “Buzz” instead of the number.
# For numbers which are multiple of 3 and 5 both, the array should have “FizzBuzz” instead of the number.

def fizzBuzz(A):
    B = []
    count3 = 0
    count5 = 0
    for i in range(1,A+1):
        count3+=1
        count5+=1
        stri = ""
        if(count3 != 3 and count5 != 5):
            B.append(i)
        else:
            if(count3 == 3):
                stri+="Fizz"
                count3 = 0
            if(count5 == 5):
                stri+="Buzz"
                count5 = 0
            B.append(stri)
    return B
    
A = 30
print(fizzBuzz(A))