"""
    #10871
    Input: N, X, A
    Output: print out integers from the list of integers A that are
            smaller than the integer X. N is just the length of the A.
"""

n, x = map(int,input().split())
a = list(map(int,input().split()))
output = []
for i in range(n):
    if a[i] < x:
        output.append(a[i])

for i in range(len(output)):
    print(output[i], end=' ')