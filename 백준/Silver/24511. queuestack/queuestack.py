import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b2 = list(map(int, input().split()))
m = int(input())
c = deque(map(int, input().split()))
b = deque()

for i in range(len(a)):
    if a[i] == 0:
        b.append(b2[i])

while len(c):
    x = 0
    b.appendleft(c.popleft())
    x = b.pop()
    print(x, end= " ")