# Description
# Find the maximum and the minimum of a list of positive numbers and return the integer division of the maximum divided by the minimum.

# Input
# Line 1 : N numbers separated by a space.

# Output
#The floor of the maximum divided by the minimum of the given numbers.

# 50 CHARACTERS

*a,=map(int,input().split())
print(max(a)//min(a))
