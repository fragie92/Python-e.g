# https://projecteuler.net/problem=4
#A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

n = 0
for i in range(999, 100, -1):
    for j in range(999, 100, -1):
        x = i * j
        if x > n:
            s = str(i * j)
            if s == s[::-1]:
                 n = i * j
print(n)
input()
