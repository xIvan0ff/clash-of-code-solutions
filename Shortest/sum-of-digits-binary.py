# Description
# Print the sum of digits of a decimal number converted to binary.
# Example: 15 in decimal => 1111 in binary, output will be 4.

# Input
# Input < 999999

# Output
# Output < 21

# 42 CHARACTERS

print(sum(map(int,bin(int(input()))[2:])))
