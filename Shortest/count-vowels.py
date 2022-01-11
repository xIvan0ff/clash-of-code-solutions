# Description
# You must output the count (case-insensitive) of all English vowels (A, E, I, O, U) in a string.

# Input
# Line 1: A string s for you to operate on.

# Output
# Line 1: A count of each vowel in alphabetical order separated by a space.

# 42 CHARACTERS

print(*map(input().lower().count,"aeiou"))
