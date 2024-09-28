# Read the number of elements
n = int(input(""))

# Read the elements and split them into a list
a = input("").split(" ")

# Determine the parity (even or odd) of the first element
x = int(a[0]) % 2

# Check if the second element has the same parity as the first
if x == int(a[1]) % 2:
    # If they have the same parity, find the first element with a different parity
    for i in range(2, n):
        if int(a[i]) % 2 != x:
            # Print the 1-based index of the element with different parity
            print(i + 1)
            break
else:
    # If the first and second elements have different parity
    # Check the parity of the third element
    if int(a[2]) % 2 == x:
        # If the third element has the same parity as the first, print 2
        print(2)
    else:
        # Otherwise, print 1
        print(1)