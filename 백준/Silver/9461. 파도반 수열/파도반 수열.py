import sys

input = sys.stdin.readline

def dp(n):
    for i in range(len(li), n+1):
        li.append(li[i-2] + li[i-3])


li = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9]  # 수열 규칙: li[i] = li[i-2] + li[i-3]
n = int(input())

for i in range(n):
    k = int(input())
    if k >= len(li):
        dp(k)
    print(li[k])