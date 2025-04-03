''' *Function assignment question*

1. Write a function called max_of_three that returns the maximum of three numbers.
2. Create a function called print_pattern that takes an integer n and prints a right-angled triangle pattern of stars with n rows.
3. Implement a function called check_prime that checks if a given number is prime. '''

# 2. Create a function called print_pattern that takes an integer n and prints a right-angled triangle pattern of stars with n rows.
def print_pattern(n):
    for i in range(1, n+1):
        print('*'*i)

print_pattern(15)
