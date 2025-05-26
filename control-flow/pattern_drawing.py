rows = 4  # Number of rows for the pyramid
row = 1
# Start from the first row
while row <= rows:
    spaces = 0 # Calculate the number of spaces
    stars = 4   # Calculate the number of stars in the current row
    while stars > 0:
        print("*", end="")
        stars -= 1

    print()  # Move to the next line after printing all stars in a row
    row += 1  # Increment the row count to move to the next row
