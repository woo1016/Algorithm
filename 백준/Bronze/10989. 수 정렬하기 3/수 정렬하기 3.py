import sys

input = sys.stdin.readline

n = int(input())
count_list = [0] * 10001
for i in range(n):
    count_list[int(input())] += 1

for i in range(len(count_list)):
    if n > 0:
        while count_list[i] > 0:
            print(i)
            count_list[i] -= 1
            n -= 1