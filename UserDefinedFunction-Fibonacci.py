'''*User - defined function assignment question* 

1. Write a function fibonacci(n) that returns the nth Fibonacci number using recursion.'''
def fibonacci(n):

    if n <= 0:

        return 0

    elif n == 1:

        return 1

    else:

        return fibonacci(n - 1) + fibonacci(n - 2)



print(fibonacci(10))  
