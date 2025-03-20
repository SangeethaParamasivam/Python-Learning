# Temperature Converter Program
def convert_temperature():
    print("Welcome to the Temperature Converter!")
    
    # Ask user for the conversion type
    choice = input("Do you want to convert from Celsius to Fahrenheit (C to F) or Fahrenheit to Celsius (F to C)? (Enter C or F): ").strip().upper()
    
    # Temperature conversion logic
    if choice == 'C':
        # Convert Celsius to Fahrenheit
        celsius = float(input("Enter temperature in Celsius: "))  # Input statement and type conversion
        fahrenheit = (celsius * 9/5) + 32  # Compound expression
        print(f"{celsius}°C is equal to {fahrenheit:.2f}°F")
        
    elif choice == 'F':
        # Convert Fahrenheit to Celsius
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))  # Input statement and type conversion
        celsius = (fahrenheit - 32) * 5/9  # Compound expression
        print(f"{fahrenheit}°F is equal to {celsius:.2f}°C")
    
    else:
        print("Invalid choice. Please enter 'C' or 'F'.")
        return
    
    # Demonstrating assignment with compound operators
    temp_value = float(input("Enter a temperature value to modify (in Celsius or Fahrenheit): "))
    operation = input("Do you want to add or subtract 5 degrees to/from it? (Enter 'add' or 'subtract'): ").strip().lower()
    
    if operation == 'add':
        temp_value += 5  # Using += operator
        print(f"New temperature after adding 5 degrees: {temp_value}")
    elif operation == 'subtract':
        temp_value -= 5  # Using -= operator
        print(f"New temperature after subtracting 5 degrees: {temp_value}")
    else:
        print("Invalid operation. Please enter 'add' or 'subtract'.")
        
# Run the converter program
convert_temperature()
