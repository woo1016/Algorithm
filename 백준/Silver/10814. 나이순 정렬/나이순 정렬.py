import sys
#input = sys.stdin.readline

n = int(input())
li = []

for i in range(n):
    li.append(input().split())
    li[i].append(i)

for i in range(len(li)):
    li[i][0] = int(li[i][0])
    li[i][2] = int(li[i][2])


li.sort(key=lambda x: (x[0], x[2]))

for i in range(len(li)):
    for j in range(2):
        print(li[i][j], end=" ")
    print()