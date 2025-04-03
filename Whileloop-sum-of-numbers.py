'''*While loop questions:*

1. Use a while loop to calculate the sum of numbers from 1 to 50
2. Write a program using a while loop to count the number of digits in a given number.
3. Write a program using a while loop to find the factorial of a number provided by the user.'''

# 1.Use a while loop to calculate the sum of numbers from 1 to 50
sum_num = 0

i = 1

while i <= 50:
    sum_num += i
    i += 1

print(f"Sum of numbers from 1 to 50 is {sum_num}")
