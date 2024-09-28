# Read the number of test cases
t = int(input())

# Initialize an empty list to store the input pairs
l = []

# Read each pair of inputs and store them in the list
for i in range(t):
    l.append(input("").split())

# Process each pair of inputs
for i in l:
    ry = int(i[0])  # Convert the first element to an integer
    li = int(i[1])  # Convert the second element to an integer
    
    # If we observe the inputs, whenever the sum of the given numbers is odd, the answer is "Alice" 
    # and when the sum is even, the answer is "Bob".

    # Check if the sum of the two integers is even or odd
    if (ry + li) % 2 == 0:
        print("Bob")  # Print "Bob" if the sum is even
    else:
        print("Alice")  # Print "Alice" if the sum is odd
