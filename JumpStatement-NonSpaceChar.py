'''*Jump statement assignment question*

1. Create a function that searches a string for the character 'x', uses break when found, and returns the position or -1 if not found.
2. Write a function that processes a list of values but immediately returns False if any value is zero.
3. Create a function that counts non-space characters in a string but uses continue to skip vowels.

3. Create a function that counts non-space characters in a string but uses continue to skip vowels.'''

def count_non_spvo(s):

    count = 0 

    vowels = "aeiouAEIOU"

    for char in s:

        if char in vowels:

            continue

        if char != ' ':

            count += 1

    return count

print(count_non_spvo("The way to succeed is to double your failure rate"))
