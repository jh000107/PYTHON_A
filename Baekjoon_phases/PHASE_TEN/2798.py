"""
    BRUTE FORCE ALGORITHM
    BLACKJACK
"""

N, M = map(int,input().split())
lst = list(map(int,input().split()))

num = 0

for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            update = lst[i] + lst[j] + lst[k]
            if update > num and update <= M:
                num = update

print(num)
