'''*Variable scope assignment questions*
1. Create a nested function where the inner function modifies a variable from the outer function using nonlocal
2. Write a program that uses a built-in function and also defines a variable with the same name.
3. Modify a global list inside a function using the global keyword.

1. Create a nested function where the inner function modifies a variable from the outer function using nonlocal'''
def counter():
    count = 0
    def inc():
        nonlocal count
        count = count+1
        return count
    return inc()
print(counter())  
