import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())
queue = deque([i + 1 for i in range(n)])
queque = deque()
yo_list = []
p = 0

while len(yo_list) < n:
    for i in range(k-p):
        p = 0
        if i == k-1:
            yo_list.append(queue.popleft())
        elif i < k-1:
            queue.append(queue.popleft())
        elif len(queue) == 0:
            p = i
            queue = queque
            break

formatted = f"<{', '.join(map(str, yo_list))}>"
print(formatted)