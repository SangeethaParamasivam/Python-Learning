'''*Function question*

1. Write a function called max_of_three that returns the maximum of three numbers.
2. Create a function called print_pattern that takes an integer n and prints a right-angled triangle pattern of stars with n rows.
3. Implement a function called check_prime that checks if a given number is prime. '''

# 1. Write a function called max_of_three that returns the maximum of three numbers.
def max_of_three(a, b, c):
    if a >= b and a >= c:
        return a  
    elif b >= a and b >= c:
        return b  
    else:
        return c  

print(max_of_three(2, 14, 7))  
