# pattern_drawing.py

# Prompt user for a positive integer
size = int(input("Enter the size of the pattern: "))

# Initialize the row counter
row = 0

# Outer loop using while
while row < size:
    # Inner loop using for to print '*' across the row
    for _ in range(size):
        print("*", end="")
    print()  # Print newline after each row
    row += 1
