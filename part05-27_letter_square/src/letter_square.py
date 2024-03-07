def print_square(layers):
    if layers > 26:
        print("Too many layers. Maximum is 26.")
        return

    center_letter = chr(ord('A') + layers - 1)

    for i in range(-layers + 1, layers):
        current_letter = chr(ord(center_letter) - abs(i))
        spaces = " " * abs(layers - abs(i) - 1)
        row = spaces + current_letter * (2 * (layers - abs(i)) - 1) + spaces
        print(row)

# Test the function with different numbers of layers
print_square(3)
print("\n")
print_square(4)
