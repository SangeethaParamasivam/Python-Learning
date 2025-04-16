'''*Jump statement assignment question*

1. Create a function that searches a string for the character 'x', uses break when found, and returns the position or -1 if not found.
2. Write a function that processes a list of values but immediately returns False if any value is zero.
3. Create a function that counts non-space characters in a string but uses continue to skip vowels.

1. Create a function that searches a string for the character 'x', uses break when found, and returns the position or -1 if not found.'''
def find_x(s):

    pos = -1

    for i in range(len(s)):

        if s[i] == 'x':

            pos = i

            break

    return pos

print(find_x("The experimental xenon exhaust extractor exceeded expectations in extreme x-ray exposure experiments"))
