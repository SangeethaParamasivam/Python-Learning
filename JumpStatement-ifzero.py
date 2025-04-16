'''*Jump statement assignment question*

1. Create a function that searches a string for the character 'x', uses break when found, and returns the position or -1 if not found.
2. Write a function that processes a list of values but immediately returns False if any value is zero.
3. Create a function that counts non-space characters in a string but uses continue to skip vowels.

2. Write a function that processes a list of values but immediately returns False if any value is zero.'''
def if_zero(num):

    for n in num:

        if n == 0:

            return False

        print(n)



print(if_zero([1, 2, 5, 0, 7, 8]))
