'''*Variable scope assignment questions*
1. Create a nested function where the inner function modifies a variable from the outer function using nonlocal
2. Write a program that uses a built-in function and also defines a variable with the same name.
3. Modify a global list inside a function using the global keyword.

3. Modify a global list inside a function using the global keyword.'''
g_list = [10, 20, 30]

def g_list_mod():

    global g_list

    g_list.append(40)

    g_list+=[50, 60]



g_list_mod()

print("Modified list: ", g_list)
