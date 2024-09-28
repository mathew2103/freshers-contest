n = int(input(""))
a = input("").split(" ")

x = int(a[0])%2
if x == int(a[1])%2:
    for i in range(2, n):
        if int(a[i])%2 != x:
            print(i+1)
            break
else:
    if int(a[2])%2 == x:
        print(2)
    else:
        print(1)