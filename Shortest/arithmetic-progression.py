# Description
# You have to find the n-th term of arithmetic progression.
# A is the first term of the arithmetic progression.
# D is the common difference of the arithmetic progression.
# 'N' stands for the term number

# Input
# Line 1 A is a positive integer.
# Line 2 D is a positive integer.
# Line 3 N is a positive integer and stand for term number.

# Output
# Output the n-th term of arithmetic progression

# 44 CHARACTERS

x=lambda:int(input())
print(x()+x()*(x()-1))
