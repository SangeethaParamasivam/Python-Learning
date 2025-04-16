'''*Recursive function assignment questions*
1. Write a recursive function to calculate a^b (a raised to the power b).
Input: a = 2, b = 4,  
 Output: 16 '''

def power (a,b):

    if b == 0:

        return 1

    else:

        return a*power(a, b-1)



print(power(6, 10))

