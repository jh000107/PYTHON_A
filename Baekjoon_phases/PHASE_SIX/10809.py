"""
    #10809
    Given a string S with only small case alphabets, print the position of alphabets where the
    the alphabet in the given string first appears.
"""

S = input()
ans = [-1] * 26
for i in range(len(S)):
    pos = ord(S[i])-97
    if ans[pos] == -1:
        ans[pos] = i

print(*ans)
