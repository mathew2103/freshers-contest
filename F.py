t = int(input(""))
l = []
for i in range(t):
    x = input("").split(" ")
    l.append(int(x[0])-int(x[1]))
for dif in l:
    if  dif >= 0 and (dif)%2 == 0:
        print("Yes")
    else:
        print("No")