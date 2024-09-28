
x = int(input())
l = []
for i in range(x):
    t = input().split(" ")
    a = int(t[0])
    b = int(t[1])
    c = int(t[2])
    l.append([a,b,c])

for x in l:
    [a,b,c] = x
    count = 0
    while(abs(a-b)/2 > c):
        if a < b:
            a += c
            b -= c
            
        elif a > b:
            b += c
            a -= c
        count += 1
            
    if a<b:
        count += 1    
        a += abs(a-b)/2
        b -= abs(a-b)/2
    elif a>b:
        count += 1
        b += abs(a-b)/2
        a -= abs(a-b)/2
    print(count)
