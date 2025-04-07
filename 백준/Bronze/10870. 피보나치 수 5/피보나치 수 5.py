import sys

input = sys.stdin.readline

def jagy(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return jagy(n-1) + jagy(n-2)

n = int(input())
print(jagy(n))