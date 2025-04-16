'''*Recursive function assignment questions*


3. Write a recursive function to print the Fibonacci series up to the nth term
Ex:
Input: n = 6  
Output: 0 1 1 2 3 5'''
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

def print_fibonacci_series(n):
    for i in range(n):
        print(fibonacci(i), end=' ')

print_fibonacci_series(10)
