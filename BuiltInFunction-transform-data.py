''' Built-in-function-question:
2. Write a function called transform_data that takes a list of numbers and performs these operations:

    -> Filter out all negative numbers (using filter())
    -> Square each remaining number (using map())
    -> Calculate the product of all resulting values (using functools.reduce()) ''' 

# in consule enter datas like : -2 3 -1 4

from functools import reduce

def transform_data():
    # Get input from the user
    values = input("Enter a list of numbers separated by spaces: ")
    
    # Convert the input string to a list of numbers
    values = list(map(float, values.split()))
    
    # Filter out all negative numbers
    positive_values = list(filter(lambda x: x >= 0, values))
    
    # Square each remaining number
    squared_values = list(map(lambda x: x ** 2, positive_values))
    
    # Calculate the product of all resulting values
    product = reduce(lambda x, y: x * y, squared_values)
    
    return {
        'filtered_values': positive_values,
        'squared_values': squared_values,
        'product': product
    }

# Example usage
result = transform_data()
print(result)

