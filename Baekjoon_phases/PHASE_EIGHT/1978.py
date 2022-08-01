"""
    #1978
    Given N integers, find the number of prime numbers.
"""
N = int(input())
lst = map(int,input().split())

def prime_num(num):
    if num == 1:
        return False
    for i in range(2, num):
        if num%i == 0:
            return False
    return True

ans = 0
for i in lst:
    if prime_num(i):
        ans += 1

print(ans)
