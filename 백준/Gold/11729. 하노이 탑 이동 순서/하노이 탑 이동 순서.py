import sys

input = sys.stdin.readline
sum = 0

def hanoi_tower(n, fro, temp, to):
    global sum
    sum += 1
    if n == 1:
        li.append([fro, to])
    else:
        hanoi_tower(n-1, fro, to, temp)
        li.append([fro, to])
        hanoi_tower(n-1, temp, fro, to)

n = int(input())
li = []
hanoi_tower(n, 1, 2, 3)
print(sum)
for i in range(len(li)):
    print(li[i][0], li[i][1])