x = input("").split(" ")
s = int(x[0])
v = int(x[1])
x = v/s
c = 0
if x != int(x):
    print(-1)
else:
    while (x != 1):
        if x % 2 == 0:
            x = x/2
            c += 1
        elif x % 3 == 0:
            x = x/3
            c += 1
        else:
            print(-1)
            break
    else:
        print(c)
