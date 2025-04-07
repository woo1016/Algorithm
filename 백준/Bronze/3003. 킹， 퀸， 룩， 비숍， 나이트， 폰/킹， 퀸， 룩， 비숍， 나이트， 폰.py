import sys

li = list(map(int, input().split()))
li[0] -= 1
li[1] -= 1
li[2] -= 2
li[3] -= 2
li[4] -= 2
li[5] -= 8

for i in range(len(li)):
    if li[i] != 0:
        li[i] *= -1

for i in range(len(li)):
    print(li[i], end=" ")