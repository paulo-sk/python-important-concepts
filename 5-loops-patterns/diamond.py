height = 6
middle = height // 2

for i in range(middle):
    print(" " * (middle - i) + "*" * (2 * i + 1))  # Adjusting spacing for even width

for i in range(middle, 0, -1):
    print(" " * (middle - i + 1) + "*" * (2 * i - 1))  # Adjusting spacing for even width
