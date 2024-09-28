# Read the number of test cases
t = int(input(""))

# Initialize an empty list to store differences
l = []

# Loop through each test case
for i in range(t):
    # Read the input and split it into two numbers
    x = input("").split(" ")
    # Calculate the difference and add it to the list
    l.append(int(x[0]) - int(x[1]))

# Loop through each difference in the list
for dif in l:
    # Check if the difference is non-negative and even
    if dif >= 0 and dif % 2 == 0:
        print("Yes")
    else:
        print("No")