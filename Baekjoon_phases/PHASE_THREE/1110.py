"""
    #1110
    Input: integer between 0 and 99, N
    Output: when N is smaller than 10, add 0 to the end and make it
    a two digit number. Then, add each digit of N, and put it together with
    the units of N. Continue doing this until you get the original N.
    Print # of times it takes.
    Ex: N = 26. 2+6 = 8. Take the units of N, which is 6, and put
    it together with 8. You get 68.
"""

n = int(input())
# returns the sum of each digit of num
def sum_digits(num):
    result = 0
    while(num>0):
        rem = num%10
        result += rem
        num = int(num/10)
    return result
x = -1
output = 0
while(x!=n):
    if n < 10:
        n = n*10    # if n is smaller than 10, make it a two digit num
    if output == 0:
        x = n
    x = x%10*10 + sum_digits(x)%10
    output += 1

print(output)

    