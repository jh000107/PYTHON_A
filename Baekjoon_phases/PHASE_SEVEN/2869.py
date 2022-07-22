"""
    #2869
    A snail wants to climb up the tree that is V m.
    The snail climbs up A m when it's bright, and falls back down
    B m when it's dark. The snail does not slip down when it reaches
    the top. How long does the snail to reach the top?
"""
"""
# Takes too much time
A,B,V = map(int,input().split())
pos = 0
day = 0
while(V>=pos):
    day += 1
    pos += A
    if pos >= V:
        break
    else:
        pos -= B
print(day)
"""

from math import ceil


A,B,V = map(int,input().split())
day = 1
if A>=V:
    print(day)
else:
    day += ceil((V-A)/(A-B))
    print(day)
