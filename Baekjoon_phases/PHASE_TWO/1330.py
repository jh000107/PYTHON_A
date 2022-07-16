"""
    #1330
    Take two inputs, A,B, and compare them
    If A>B, print '>'
    if A<B, print '<'
    if A=B, print '=='
"""

a,b = map(int,input().split())
if a>b:
    print('>')
elif a<b:
    print('<')
else:
    print('==')
