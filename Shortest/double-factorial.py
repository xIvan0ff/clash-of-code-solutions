# Description
# You are given a number n, you are to determine its double factorial
# double factorial of a number means the number * (number-2) * (number-4) * .... till 1 or 2 depending on whether it's even or not

# Missing Input/Output data

# 48 CHARACTERS
f=lambda n:n<1or n*f(n-2)
print(f(int(input())))
