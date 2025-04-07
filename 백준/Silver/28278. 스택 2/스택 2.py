import sys

input = sys.stdin.readline
sta = []
li = []

def stack(command):
    if command == 2:
        if len(sta) == 0:
            print(-1)
        else:
            print(sta.pop())
    elif command == 3:
        print(len(sta))
    elif command == 4:
        if len(sta) == 0:
            print(1)
        else:
            print(0)
    elif command == 5:
        if len(sta) == 0:
            print(-1)
        else:
            print(sta[-1])

for i in range(int(input())):
    k = input().strip().split()
    if len(k) == 2:
        k = list(map(int, k))
        sta.append(int(k[1]))
    else:
        k = int(k[0])
        stack(k)