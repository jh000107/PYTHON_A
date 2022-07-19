"""
    #10818
    First line input: number of integers
    Second line input: list of integers
    Output: Print minimum and maximum number
"""

n = int(input())
lst = list(map(int,input().split()))
min = lst[0]
max = lst[0]

for i in range(1,n):
    if lst[i] > max:
        max = lst[i]
    if lst[i] < min:
        min = lst[i]

print(min, max)