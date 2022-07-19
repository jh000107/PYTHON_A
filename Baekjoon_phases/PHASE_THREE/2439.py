"""
    #2439
    Similar to Question #2438. The difference is that it prints the
    stars right-sided
"""

n = int(input())
for i in range(1,n+1):
    print(" " * (n-i) + "*"*i)
