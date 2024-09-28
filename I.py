# Read an integer input
x = int(input())

# Initialize an empty list to store the input values
l = []

# Loop to read 'x' number of inputs
for i in range(x):
    # Split the input string into a list of strings
    t = input().split(" ")
    # Convert the strings to integers
    a = int(t[0])
    b = int(t[1])
    c = int(t[2])
    # Append the integers as a list to 'l'
    l.append([a, b, c])

# Loop through each list in 'l'
for x in l:
    # Unpack the list into variables a, b, and c
    [a, b, c] = x
    # Initialize the count of operations
    count = 0
    
    # Loop until the absolute difference between 'a' and 'b' divided by 2 is greater than 'c'
    while abs(a - b) / 2 > c:
        # If 'a' is less than 'b', increase 'a' by 'c' and decrease 'b' by 'c'
        if a < b:
            a += c
            b -= c
        # If 'a' is greater than 'b', decrease 'a' by 'c' and increase 'b' by 'c'
        elif a > b:
            b += c
            a -= c
        # Increment the count of operations
        count += 1
    
    # If 'a' is still less than 'b' after the loop
    if a < b:
        count += 1
        # Adjust 'a' and 'b' to make them equal
        a += abs(a - b) / 2
        b -= abs(a - b) / 2
    # If 'a' is still greater than 'b' after the loop
    elif a > b:
        count += 1
        # Adjust 'a' and 'b' to make them equal
        b += abs(a - b) / 2
        a -= abs(a - b) / 2
    
    # Print the count of operations
    print(count)
