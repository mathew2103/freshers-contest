# Read input and split it into a list of strings
x = input("").split(" ")

# Convert the first and second elements of the list to integers
s = int(x[0])
v = int(x[1])

# Calculate the ratio of v to s
x = v / s

# Initialize a counter for the number of operations
c = 0

# Check if the ratio is not an integer
if x != int(x):
    # If not, print -1 and exit
    print(-1)
else:
    # While the ratio is not equal to 1
    while x != 1:
        # If the ratio is divisible by 2
        if x % 2 == 0:
            # Divide the ratio by 2 and increment the counter
            x = x / 2
            c += 1
        # If the ratio is divisible by 3
        elif x % 3 == 0:
            # Divide the ratio by 3 and increment the counter
            x = x / 3
            c += 1
        else:
            # If the ratio is not divisible by 2 or 3, print -1 and exit
            print(-1)
            break
    else:
        # If the loop completes, print the counter
        print(c)
