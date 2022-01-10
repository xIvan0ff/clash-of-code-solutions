# A Japanese comedian once showed a joke that when you speak out a number which is a multiple of 3 or which contains the digit 3, it becomes dope. Let's try to implement it this time.

# In the input, two integers are given. In the output, count up from the first integer to the second integer.
# However, if the number is a multiple of 3 (3, 6, 9, 12, etc.), or if any digit has 3 in it (13, 23, 30, 31, etc.), output "Dope".

# Input
# An integer N1 to start counting up and an integer N2 to end counting up.

# Output
# The string to use when counting up. Put a "-" between each count.

# 100 CHARACTERS

s,e=map(int,input().split())
print(*[[i,"Dope"]['3'in str(i)or i%3<1]for i in range(s,e+1)],sep="-")
