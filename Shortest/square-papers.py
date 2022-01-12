# Description
# You have given 2 square papers. Join the squares to make a Rectangle (you can cut the extra part) find the area of resulting Rectangle .

# Input
# Line 1 X is the side of the square 1
# Line 2 Y is the side of the square 2

# Output
# Output the area of resulting rectangle.

# 41 CHARACTERS

*l,=map(int,open(0))
print(min(l)*sum(l))
