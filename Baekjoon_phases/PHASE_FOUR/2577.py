"""
    #2577
    Given three integers, A, B, and C, multiply them and print how many times 0~9 appear.
    For example,
        A=150, B=266, C=427
        AXBXC = 17037300
        0 is used 3 times, 1 is used once, 3 is used twice, 7 is used twice
"""
lst = []
for i in range(3):
    num = int(input())
    lst.append(num)

mul = 1 #initial value of mul
for i in range(len(lst)):
    mul = mul * lst[i]

result = [0] * 10 # set 0 times for 0~9 used
while(mul > 0):
    rem = mul % 10
    result[rem] += 1
    mul = int(mul/10)

for i in range(len(result)):
    print(result[i])
