# Description
# A Harshad number is an integer that is divisible by the sum of its own digits.
# For example, 1729 is a Harshad number because 1 + 7 + 2 + 9 = 19 and 1729 = 19 × 91.

# Input
# A positive integer N.

# Output
# true if the integer is a Harshad number.
# false If the integer is not a Harshad number.

# 53 CHARACTERS

print(str(int(s:=input())%sum(map(int,s))<1).lower())
