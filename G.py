# Solution by AbelAbraham77

def when_scolding(m, o, p):
    # Calculate the total number of tiffins
    total = m + o + p
    
    # Calculate the maximum number of days they can be scolded
    max_days = total // 2
    
    # Find the maximum number of tiffins among the three
    max_tiffins = max(m, o, p)
    
    # If the maximum tiffins is greater than the sum of the other two,
    # return the difference, otherwise return max_days
    if max_tiffins > (total - max_tiffins):
        return total - max_tiffins
 
    return max_days
 
# Read the number of test cases
n = int(input())
list1 = []

# Process each test case
for i in range(n):
    data = input().split()
    m = int(data[0])
    o = int(data[1])
    p = int(data[2])
 
    # Append the result of when_scolding to the list
    list1.append(when_scolding(m, o, p))
 
# Print the results for all test cases
for result in list1:
    print(result)