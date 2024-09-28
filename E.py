from math import ceil

n = int(input(""))
l = []
for i in range(n):
    l.append(int(input("")))

for i in range(n):
    if l[i] <= 4:
        print(1)
    else:
        print(ceil(l[i]/4))