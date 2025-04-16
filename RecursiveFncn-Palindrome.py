'''*Recursive function assignment questions*

2. Write a recursive function to check if a string is a palindrome.

Input: "madam"
Output: True'''

def is_palindrome(s):

    if len(s) <= 1:

        return True

    if s[0] !=s[-1]:

        return False

    

    return is_palindrome(s[1:-1])



print(is_palindrome("fibonacci"))
