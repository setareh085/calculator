def get_number(prompt="Enter a number: "):
    """Force user to enter a valid number (int)."""
    while True:
        value = input(prompt)
        try:
            return int(value)
        except ValueError:
            print("Invalid input! Please enter a number.")

def is_empty(lst):
    """Check if the given list is empty."""
    return len(lst) == 0

