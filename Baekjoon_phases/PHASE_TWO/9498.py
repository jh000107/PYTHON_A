"""
    #9498
    Take a test score as an input, and
    print 90~100 as A, 80~89 as B, 70~79 as C, 60~69 as D, and F for else.
"""

score = int(input())
if score>=90:
    print('A')
elif score>=80:
    print('B')
elif score>=70:
    print('C')
elif score>=60:
    print('D')
else:
    print('F')
