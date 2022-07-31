"""
    #11653
    Prime Factorization. Prime Factorize the integer N.
"""

N = int(input())
# helper function

def prime_num(num):
    if num == 1:
        return False
    for i in range(2, num):
        if num%i == 0:
            return False
    return True


while(N >= 1):
    if N == 1:
        break
    for i in range(2,N+1):
        if prime_num(i) and N%i==0:
            N = int(N/i)
            print(i)
            break
    
