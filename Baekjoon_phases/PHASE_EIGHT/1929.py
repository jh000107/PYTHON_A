"""
    #1929
    Find a prime number, but a faster version. The key point is, when deciding whether a number is prime or not, you only have to check until the squre root of
    the given number.
"""
import math

def prime_num(num):
    if num == 1:
        return False
    sq = int(math.sqrt(num))
    for i in range(2, sq+1):
        if num%i == 0:
            return False
    return True

M, N = map(int,input().split())
for i in range(M,N+1):
    if prime_num(i):
        print(i)