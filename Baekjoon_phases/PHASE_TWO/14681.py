"""
    #14681
    This question takes two inputs, one for x coordinate and
    one for y coordinate. The question prints out the quadrant.
"""

x = int(input())
y = int(input())

# When x coordinate is positive
if x >= 0:
    if y >= 0:
        print(1)
    else:
        print(4)
# When x coordinate is negative
else:
    if y >= 0:
        print(2)
    else:
        print(3)
    