# Description
# Write a program that prints the sum of all the positive multiples of 3 or 5 or 7 below N.
# For example, if N=15 we get 3, 5, 6, 7, 9, 10, 12, 14 and the sum of these multiples is 66.

# Input
# A positive number N

# Output
# The sum of all the positive multiples of 3 or 5 or 7 below N

# 73 CHARACTERS

print(sum(x if x%3<1or x%5<1or x%7<1else 0 for x in range(int(input()))))
