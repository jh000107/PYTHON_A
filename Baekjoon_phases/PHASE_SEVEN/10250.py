"""
    #10250
    ACM HOTEL
"""

T = int(input())

for i in range(T):
    H,W,N = map(int,input().split())
    if N % H == 0:
        f = H * 100
        ho = N // H
    else:
        f = (N%H) * 100
        ho = 1+N//H
    print(f+ho)