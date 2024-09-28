l = int(input(""))
s = input("").lower()
a = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split(" ")
 
for i in range(l):
    a[ord(s[i]) - 97] = " "

if " "*26 == "".join(a):
    print("YES")
else:
    print("NO")