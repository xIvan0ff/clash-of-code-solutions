# Description
# You must output the sum of the digits of the exponentiation of two input numbers.

# Input
# Line 1: An integer X for the base.
# Line 2: An integer Y for the exponent.

# Output
# A single line containing the sum of all digits from the result of X^Y

# 48 CHARACTERS

f=input
f(sum(map(int,str(int(f())**int(f())))))
