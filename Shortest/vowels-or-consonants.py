# Description
# You will have to determine if the input string has more vowels or consonants.
# y is a vowel

# Input
# A string to inspect
# Output
# Print consonants if there are more consonants in string, print vowels else.

# 78 CHARACTERS

print("consonants"if len(a:=input())>2*sum(map(a.count,"aeiouy"))else"vowels")
