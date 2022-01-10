# Description
# Given an integer N, you have to return the difference D between the sum of the digits at even positions (first digit at position 0) and the sum of the digits at odd positions.

# Input
# Line 1 : An integer N
 
# Output
# Line 1 : D = Sum of digits at even positions - Sum of digits at odd positions

# 52 CHARACTERS

i=list(map(int,input()))
print(2*sum(i[::2])-sum(i))
