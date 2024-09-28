# Solution by AbelAbraham77

def when_scolding(m, o, p):
    total = m + o + p
    
    max_days = total // 2
    max_tiffins = max(m, o, p)
    
    if max_tiffins > (total - max_tiffins):
        return total - max_tiffins
 
    return max_days
 
n = int(input())
list1 = []
for i in range(n):
    data = input().split()
    m = int(data[0])
    o = int(data[1])
    p = int(data[2])
 
    list1.append(when_scolding(m, o, p))
 
for result in list1:
    print(result)