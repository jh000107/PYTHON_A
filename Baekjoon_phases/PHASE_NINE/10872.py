"""
    #10872
    Factorial: use a recursive function
"""

N = int(input())

def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial (n-1)

print(factorial(N))
