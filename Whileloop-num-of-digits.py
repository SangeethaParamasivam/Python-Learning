''' *While loop questions:*

1. Use a while loop to calculate the sum of numbers from 1 to 50
2. Write a program using a while loop to count the number of digits in a given number.
3. Write a program using a while loop to find the factorial of a number provided by the user. '''

# 2. Write a program using a while loop to count the number of digits in a given number.

digit = str(input("Enter number to count digit: "))

index = 0

while index < len(digit):

    index += 1

print("Digit count: ", len(digit))
