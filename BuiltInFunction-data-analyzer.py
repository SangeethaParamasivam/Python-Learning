'''*Built-in Function Question*

1. Write a function called data_analyzer that processes a list of numeric values and returns a dictionary with the following information:

    -> The sum of all values (using the appropriate built-in function)
    -> The minimum and maximum values (using appropriate built-in functions)
    -> The average (mean) of all values (calculate this using built-in functions)
    -> The number of values that are above the average
    -> A sorted version of the original list (using the appropriate built-in function) '''

def data_analyzer():
    # Get input from the user
    values = input("Enter a list of numeric values separated by spaces: ")
    
    # Convert the input string to a list of numbers
    values = list(map(float, values.split()))
    
    # Calculate the sum of all values
    total_sum = sum(values)
    
    # Find the minimum and maximum values
    min_value = min(values)
    max_value = max(values)
    
    # Calculate the average (mean) of all values
    average = total_sum / len(values)
    
    # Count the number of values that are above the average
    above_average_count = len([value for value in values if value > average])
    
    # Sort the original list
    sorted_values = sorted(values)
    
    # Create a dictionary with the required information
    result = {
        'sum': total_sum,
        'min': min_value,
        'max': max_value,
        'average': average,
        'above_average_count': above_average_count,
        'sorted_values': sorted_values
    }
    
    return result

# Example usage
result = data_analyzer()
print(result)


