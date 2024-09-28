from math import ceil  # Import the ceil function from the math module

# Read the number of elements
n = int(input(""))

# Initialize an empty list to store the elements
l = []
for i in range(n):
    # Read each element and append it to the list
    l.append(int(input("")))

# Iterate over each element in the list
for i in range(n):
    if l[i] <= 4:
        # If the element is less than or equal to 4, print 1
        print(1)
    else:
        # Otherwise, print the ceiling of the element divided by 4
        print(ceil(l[i] / 4))