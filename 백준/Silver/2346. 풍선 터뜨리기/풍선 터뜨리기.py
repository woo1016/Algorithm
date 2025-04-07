import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))
deq = deque((i + 1, numbers[i]) for i in range(n))
result = []

idx, move = deq.popleft()
result.append(idx)

while deq:
    if move > 0:
        for _ in range(move-1):
            deq.append(deq.popleft())
    else:
        for _ in range(abs(move)):
            deq.appendleft(deq.pop())

    idx, move = deq.popleft()
    result.append(idx)

print(" ".join(map(str, result)))