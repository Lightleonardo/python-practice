def read_int(prompt):
    """Reads an integer from the user until a valid integer is entered."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a whole number.")

def safe_divide(a, b):
    """Safely divides two numbers, returning None if division by zero occurs."""
    try:
        return a / b
    except ZeroDivisionError:
        return None

# Demonstration of both functions
if __name__ == "__main__":
    # Using read_int function
    try:
        number = read_int("Please enter a number: ")
        print(f"The number you entered is: {number}")
    except ValueError:
        print("There was an error. Please enter a valid number.")

    # Using safe_divide function
    try:
        a = 10
        b = 2
        result = safe_divide(a, b)
        print(f"The result of {a} divided by {b} is: {result}")
    except ZeroDivisionError:
        print("Cannot divide by zero!")