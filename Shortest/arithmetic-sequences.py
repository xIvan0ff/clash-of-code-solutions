# Description 
# Given integer n,a and b print the first n terms of the arithmetic sequence starting from a+b and with common difference a.

#a+b, 2*a+b, ... , n*a+b

# Input
# line 1 : Integer n
# line 2 : space separated integers a and b

# Output
# n lines of integers

# 70 Description

n,a,b=map(int,open(0).read().split())
for i in range(n):print(a+b+i*a)
