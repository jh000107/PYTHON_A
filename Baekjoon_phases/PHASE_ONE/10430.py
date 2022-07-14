"""
    #10430
    Take 3 inputs: A,B,C
    The question is asking to see if
    (A+B)%C =? ((A%C)+(B%C))%C
    (AXB)%C =? ((A%C)X(B%C))%C
"""

a,b,c = map(int,input().split())
first = (a+b)%c
second = ((a%c)+(b%c))%c
third = (a*b)%c
fourth = ((a%c)*(b%c))%c
print(first, '\n',second, '\n', third, '\n', fourth, sep='')