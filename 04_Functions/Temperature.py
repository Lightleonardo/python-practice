# Convert Celsius to Fahrenheit
# Ensure the function uses absolute tolerance for floating-point comparison
def celsius_to_fahrenheit(c):
    fahrenheit = (c * 9/5) + 32
    return fahrenheit

# Convert Fahrenheit to Celsius
def fahrenheit_to_celsius(f):
    celsius = (f - 32) * 5/9
    return celsius
    

if __name__ == "__main__":
    c = float(input("Enter a temperature in Celsius: "))
    print(f"{c} C = {celsius_to_fahrenheit(c):.1f} F")

    f = float(input("Enter a temperature in Fahrenheit: "))
    print(f"{f} F = {fahrenheit_to_celsius(f):.1f} C")