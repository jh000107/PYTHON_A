"""
    #1712: BREAK-EVEN POINT
    Create a program that calculates the BREAK-EVEN POINT
"""

# This code works, but takes too much time.
"""
A,B,C = map(int,input().split())
num_sales = 0
cost = A #initial value of total costs
sales = 0 #initial value of total sales
while(cost>sales):
    if B>=C: #case when always down
        num_sales = -1
        break
    cost = A+B*num_sales
    sales = C*num_sales
    print(cost, sales)
    num_sales += 1

print(num_sales)
"""
# use simple math
A,B,C = map(int,input().split())
if B>=C:
    print(-1)
else:
    print(int(A/(C-B)+1))