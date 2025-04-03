''' *Function assignment question*

1. Write a function called max_of_three that returns the maximum of three numbers.
2. Create a function called print_pattern that takes an integer n and prints a right-angled triangle pattern of stars with n rows.
3. Implement a function called check_prime that checks if a given number is prime. '''

# 3. Implement a function called check_prime that checks if a given number is prime.

def check_prime(num):
    if num == 0 or num == 1:
        return "Not a prime"
    elif num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return "Not a prime"
        else:
            return "Is a prime"

print(check_prime(2))
