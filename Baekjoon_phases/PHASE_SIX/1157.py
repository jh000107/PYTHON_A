"""
    #1157
    Given a string, find out which alphabet is used the most when
    lower and upper case letters are treated equal.
"""

word = input().lower() # convert it to lower case letters
num_used = [0] * 26
for character in word:
    idx = ord(character)-ord('a')
    num_used[idx] += 1

most_used = max(num_used)
num = 0
pos = 0
for i in range(len(num_used)):
    if num_used[i] == most_used:
        num += 1
        pos = i

if(num>1):
    print('?')
else:
    print(chr(pos+ord('a')).upper())
