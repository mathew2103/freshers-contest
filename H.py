t = int(input())
l = []
for i in range(t):
    l.append(input("").split())

for i in l:
    ry = int(i[0])
    li = int(i[1])
    if (ry + li) % 2 == 0:
        print("Bob")
    else:
        print("Alice")

