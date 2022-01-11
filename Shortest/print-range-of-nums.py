# Description
# You are given a number n. The number n can be negative or positive. If n is negative, print numbers from n to 0 by adding 1 to n. If positive, print numbers from n-1 to 0 by subtracting 1 from n.

# Input
# Given a number n.

# Output
# If n is negative, print numbers from n to 0 by adding 1 to n. If positive, print numbers from n-1 to 0 by subtracting 1 from n. If n=0 then print "Already Zero".


# XXX Characters

I=input
n=int(I())
if n==0:I("Already Zero")
if n>0:n-=1
a=n<0 or-1
print(*range(n,a,a))
