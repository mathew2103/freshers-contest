# Take the first input from the user and convert it to lowercase
a = input("").lower()

# Take the second input from the user and convert it to lowercase
b = input("").lower()

# Compare the two strings lexicographically
if a < b:
    # If the first string is less than the second, print -1
    print(-1)
elif a > b:
    # If the first string is greater than the second, print 1
    print(1)
else:
    # If both strings are equal, print 0
    print(0)
