"""
    #2562
    Given 9 different integers, find out the maximum integer and its position as well.
"""

# used to create a list containing all 9 integers
lst = []
for i in range(9):
    inputs = int(input())
    lst.append(inputs)

max = lst[0]
pos = 1
for i in range(1,len(lst)):
    if lst[i] > max:
        max = lst[i]
        pos = i+1

print(max)
print(pos)