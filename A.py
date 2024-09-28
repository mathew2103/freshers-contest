a = input("").lower()
b = input("").lower()

if a<b:
    print(-1)
elif a>b:
    print(1)
else:
    print(0)

for i in range(len(a)):
    if a[i] < b[i]:
        print(-1)
        break
    elif a[i] > b[i]:
        print(1)
        break 
else:
    print(0)