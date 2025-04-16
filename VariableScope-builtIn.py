'''*Variable scope assignment questions*
1. Create a nested function where the inner function modifies a variable from the outer function using nonlocal
2. Write a program that uses a built-in function and also defines a variable with the same name.
3. Modify a global list inside a function using the global keyword.

2. Write a program that uses a built-in function and also defines a variable with the same name.'''

numbers = [1, 2, 3, 4, 5]

total = sum(numbers)  

print("Total using built-in sum:", total)



sum = 42

print("Redefined 'sum' as variable:", sum)
