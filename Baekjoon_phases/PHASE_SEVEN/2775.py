"""
    #2775
    부녀회장이 될테야!
"""

T = int(input())

for i in range(T):
    floor = int(input())
    num = int(input())
    f = [x for x in range(1,num+1)]
    for j in range(floor):
        for k in range(1, num):
            f[k] += f[k-1]
    print(f[-1])
