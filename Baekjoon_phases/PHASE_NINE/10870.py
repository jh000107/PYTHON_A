"""
    #10870
    Fibonacci Sequence 5
    Given N, solve for fibonacci sequence using recursive function.
"""

N = int(input())

def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci(num-1) + fibonacci(num-2)

print(fibonacci(N))