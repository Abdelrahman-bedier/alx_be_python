FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return fahrenheit * (FAHRENHEIT_TO_CELSIUS_FACTOR - 32)

def convert_to_fahrenheit(celsius):
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32

temperature = input("Enter the temperature to convert: ")
unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

try:
    if unit == "F":
        output_temperature = convert_to_celsius(temperature)
        print(f"{temperature}°F is {output_temperature}°C")
    elif unit == "C":
        output_temperature = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {output_temperature}°F")
    else:
        print("Invalid temperature. Please enter a numeric value.")
except:
    print("Invalid temperature. Please enter a numeric value.")