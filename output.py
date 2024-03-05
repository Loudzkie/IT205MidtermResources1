def print_pattern(n):
    for i in range(1, n + 1):
        print('* ' * i)
    
    for i in range(n - 1, 0, -1):
        print('* ' * i)

# Set the number of rows
rows = 5

# Call the function to print the pattern
print_pattern(rows)
