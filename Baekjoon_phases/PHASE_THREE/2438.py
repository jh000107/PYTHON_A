"""
    #2438
    Input: N max stars that the program will reach
    Output: prints a star line by line that increases gradually until
            it reaches N stars
            *
            **
            ***...
"""
n = int(input())
for i in range(1,n+1):
    print(i * '*')
