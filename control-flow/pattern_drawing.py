size = int(input("Enter the size of the pattern: "))

# Check if input is a positive integer
if size <= 0:
    print("Please enter a positive integer.")
else:
    row = 0
    # While loop to iterate through each row
    while row < size:
        # For loop to print asterisks side by side
        for i in range(size):
            print("*", end="")
        # Print newline after each row
        print()
        row += 1
