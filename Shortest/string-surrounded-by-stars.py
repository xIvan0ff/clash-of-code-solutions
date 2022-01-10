# DESCRIPTION:
# You must print the string A surrounded by asterisks to form a box. 

# Input
#A The string

# Output
# Line 1 Length of A+4 stars
# Line 2 A star followed by a space, then the string, another space and a final star.
# Line 3 Length of A+4 stars

# 51 CHARACTERS

f="*"*(len(a:=input())+4)
print(f+f"\n* {a} *\n"+f)
