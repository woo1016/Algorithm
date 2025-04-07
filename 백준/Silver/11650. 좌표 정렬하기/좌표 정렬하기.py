import sys
input = sys.stdin.readline

n = int(input())
li = []

for i in range(n):
    li.append(list(map(int, input().split())))

li.sort()
for i in range(n):
    for j in range(2):
        print(li[i][j], end=" ")
    print()