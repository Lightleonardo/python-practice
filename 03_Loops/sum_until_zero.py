#initialize the sum
total_sum = 0

# Start the loop
while True:
    # Ask the user for input
    number = int(input("Enter a number (or 0 to stop): "))

    # Check if the user wants to stop
    if number == 0:
        break

    # Add the number to the total sum
    total_sum += number

# Print the total sum
print(f"The sum of the numbers entered is: {total_sum}")