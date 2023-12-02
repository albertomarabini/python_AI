# Example tuple
kata = (19, 42, 21)

def display_numbers(numbers):
    num_count = len(numbers)
    formatted_numbers = ", ".join(map(str, numbers))
    return f"The {num_count} numbers are: {formatted_numbers}"

# Displaying the formatted result
print(display_numbers(kata))