"""
    #2908
    Input: Two integers A and B
    output: When two integers(100<=A,B<=999) are reversed, find the bigger one
"""

A, B = input().split()
# Reverse A,B and convert them to integers for the comparison
A = int(A[::-1]) 
B = int(B[::-1])

if A>B:
    print(A)
else:
    print(B)

