"""
    #2480
    You are rolling 3 dice.
    If you get three same numbers, you get 10,000 + the number*1,000
    If you get two same numbers and different, you get 1,000 + the number*100
    If you get all different numbers, you get the biggest number*100
"""

a,b,c = map(int,input().split())
if a==b and b==c:
    print(10000+1000*a)
elif (a==b and a!=c) or (a==c and a!=b):
    print(1000+100*a)
else:
    print(100*max(a,b,c))