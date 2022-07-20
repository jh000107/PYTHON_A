"""
    #15596
    Create a function that returns thesum of a list of integers
"""

def solve(a):
    sum = 0
    for i in range(len(a)):
        sum += a[i]
    return sum