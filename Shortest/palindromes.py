# Description
# A palindrome is a piece of text where the order of the letters stay the same whether you read from left to right or right to left.
# Your program must output whether, for each word given on the standard input, where it is a palindrome or not.
# A single letter is considered to be a palindrome.

# Input
# Line 1: the number N of words
# N next lines: a word W to analyze

# Output
# For each word, true if W is a palindrome, false otherwise.

# 55 CHARACTERS

input()
while a:=input():print(str(a==a[::-1]).lower())
