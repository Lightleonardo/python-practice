def calculate_total(items):
    """Calculates the total price of the shopping list."""
    return sum(item[1] for item in items)

def find_most_expensive(items):
    """Finds the most expensive item in the shopping list."""
    return max(items, key=lambda item: item[1])

def format_receipt(items):
    """Formats a shopping receipt as a multi-line string."""
    receipt = ""
    for item in items:
        receipt += f"{item[0]}: ${item[1]:.2f}\n"
    return receipt.strip()

# Constants (in UPPER_CASE)
CURRENCY_SYMBOL = "$"
SHOPPING_LIST = [
    ("Apples", 1.5),
    ("Bananas", 0.75),
    ("Cookies", 2.5),
    ("Dairy Milk", 3.5),
    ("Rice", 1.5)
]

# Main function
def main():
    """Main function to run the shopping summary program."""
    items = SHOPPING_LIST  # Initialize with the provided list

    total_price = calculate_total(items)
    print(f"Total Price: ${total_price:.2f}")

    most_expensive_item = find_most_expensive(items)
    print(f"The most expensive item is: {most_expensive_item[0]} - ${most_expensive_item[1]:.2f}")

    receipt = format_receipt(items)
    print(receipt)

if __name__ == "__main__":
    main()