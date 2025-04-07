import sys
from collections import deque
input = sys.stdin.readline

deq = deque()
def queue_command(x):
    if x[0] == 1:
        deq.appendleft(x[1])
    elif x[0] == 2:
        deq.append(x[1])
    elif x[0] == 3:
        if len(deq):
            print(deq.popleft())
        else:
            print(-1)
    elif x[0] == 4:
        if len(deq):
            print(deq.pop())
        else:
            print(-1)
    elif x[0] == 5:
        print(len(deq))
    elif x[0] == 6:
        if len(deq):
            print(0)
        else:
            print(1)
    elif x[0] == 7:
        if len(deq):
            print(deq[0])
        else:
            print(-1)
    elif x[0] == 8:
        if len(deq):
            print(deq[-1])
        else:
            print(-1)

for i in range(int(input())):
    command = list(map(int, input().split()))
    queue_command(command)