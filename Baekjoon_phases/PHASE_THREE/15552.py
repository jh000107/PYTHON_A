"""
    #15552
    For the first line, you are going to take the number of test cases T.
    Then, you are going to get T rows of integers, A and B.
    Print sum of each row.
"""

# Importing sys for better efficiency when reading in test cases
import sys

t = int(sys.stdin.readline())
answer = []
for i in range(t):
    a,b = map(int,sys.stdin.readline().split())
    answer.append(a+b)

for i in range(len(answer)):
    print(answer[i])
