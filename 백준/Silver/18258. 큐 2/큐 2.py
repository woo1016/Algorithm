import sys
from collections import deque

input = sys.stdin.readline
queue = deque()

def find_command(command):
    len_queue = len(queue)
    if command == "pop":
        if len_queue == 0:
            return -1
        else:
            return queue.popleft()
    elif command == "size":
        return len_queue
    elif command == "empty":
        if len_queue == 0:
            return 1
        else:
            return 0
    elif command == "front":
        if len_queue == 0:
            return -1
        else:
            return queue[0]
    elif command == "back":
        if len_queue == 0:
            return -1
        else:
            return queue[-1]


for i in range(int(input())):
    commands = input().split()

    if commands[0] == 'push':
        commands[1] = int(commands[1])
        queue.append(commands[1])
    else:
        a = find_command(commands[0])
        sys.stdout.write(f"{a}\n")
