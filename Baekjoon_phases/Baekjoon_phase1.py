"""
    #2557
    Print Hello World!
"""
print('Hello World!')

"""
    #10718
    Print "강한친구 대한육군" twice. Once in each row
"""

print('강한친구 대한육군')
print('강한친구 대한육군')

"""
    #1000
    Take two inputs, and print the sum
"""

a, b= map(int, input().split())
print(a+b)


"""
    #10926
    Put ??! after whatever the input is
"""

name = input()
print(name + "??!")

"""
    #18108
    서기 연도 vs 불기 연도
"""

bulgi = int(input())
print(bulgi-543)


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