import sys

input = sys.stdin.readline

def recursion(s, l, r, c):
    c += 1
    if l >= r: return 1, c
    elif s[l] != s[r]: return 0, c
    else: return recursion(s, l+1, r-1, c)

def isPalindrome(s,c):
    return recursion(s, 0, len(s)-1, c)

for i in range(int(input())):
    s = input().strip()
    count = 0
    on = isPalindrome(s,count)
    print(on[0], on[1])