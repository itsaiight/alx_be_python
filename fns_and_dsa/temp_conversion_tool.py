FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
def convert_celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

Temperature = int(input("Enter the temperature to convert: "))
unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()
if unit == 'C':
    converted_temp = convert_celsius_to_fahrenheit(Temperature)
    print(f"{Temperature}°C is {converted_temp:.2f}°F")
elif unit == 'F':
    converted_temp = convert_fahrenheit_to_celsius(Temperature)
    print(f"{Temperature}°F is {converted_temp:.2f}°C")
else:
    print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

