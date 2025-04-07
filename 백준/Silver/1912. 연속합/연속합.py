import sys

input = sys.stdin.readline

def dp(): #카데인 알고리즘
    mx = 0
    sol = [0] * n
    for i in range(n):
        sol[i] = max(sol[i-1] + li[i],  li[i])
    print(max(sol))

n = int(input())
li = list(map(int, input().split()))
dp()