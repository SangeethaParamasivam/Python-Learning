'''*Lamba function assignment questions*
1. Write a lambda function that returns a function to calculate x^n, where n is given at runtime.'''
power = lambda n: lambda x: x**n

n = int(input("Enter n value: "))



caLc = power(n)

x = int(input("Enter x value: "))



print(caLc(x))
