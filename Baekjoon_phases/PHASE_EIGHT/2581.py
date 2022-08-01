"""
    #2581
    More prime numbers. Given two integers M, N, find the sum of all prime numbers between them, including M and N. Also, find the min prime number
"""
M = int(input())
N = int(input())
lst = []
# Brought helper function from prev question
def prime_num(num):
    if num == 1:
        return False
    for i in range(2, num):
        if num%i == 0:
            return False
    return True

for i in range(M, N+1):
    if prime_num(i):
        lst.append(i)

if len(lst) == 0:
    print(-1)
else:
    print(sum(lst))
    print(min(lst))
