'''*While loop assignment questions:*

1. Use a while loop to calculate the sum of numbers from 1 to 50
2. Write a program using a while loop to count the number of digits in a given number.
3. Write a program using a while loop to find the factorial of a number provided by the user.'''

# 3. Write a program using a while loop to find the factorial of a number provided by the user.

n = int(input("Enter a number: "))
fact = 1
i = 1

while i <= n:
    fact *= i
    i += 1

print(f"Factorial of {n} is {fact}")
