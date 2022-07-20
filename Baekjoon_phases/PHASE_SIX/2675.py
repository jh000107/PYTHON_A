"""
    #2675
    Take the string S, repeat R times, and make the new string P and print it.
"""

N = int(input())
ans = []
for i in range(N):
    P = ''
    user_input = input().split()
    for cha in user_input[1]:
        P += cha*int(user_input[0])
    ans.append(P)

print(*ans, sep='\n')