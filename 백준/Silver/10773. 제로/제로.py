import sys

input = sys.stdin.readline

stack = []
for i in range(int(input())):
    num = int(input())
    if num == 0:
        stack.pop()
    else:
        stack.append(num)

n = 0
for i in stack:
    n += i
print(n)