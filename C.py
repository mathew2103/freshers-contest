# Read the length of the string
l = int(input(""))

# Read the string and convert it to lowercase
s = input("").lower()

# Create a list of all lowercase alphabet letters
a = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split(" ")

# Iterate over each character in the string
for i in range(l):
    # Replace the corresponding alphabet character with a space
    a[ord(s[i]) - 97] = " "

# Check if all characters in the alphabet have been replaced with spaces
if " " * 26 == "".join(a):
    print("YES")
else:
    print("NO")