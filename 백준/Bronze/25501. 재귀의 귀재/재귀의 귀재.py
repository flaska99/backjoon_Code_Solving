import sys

def recursion(s, l, r, count):
    if l >= r: return print(1, count)
    elif s[l] != s[r]: return print(0, count)
    else: 
        count += 1
        return recursion(s, l+1, r-1, count)

def isPalindrome(s,c):
    return recursion(s, 0, len(s)-1, count)

t = int(input())
for i in range(t) :
    a = input()
    count = 1
    isPalindrome(a, count)