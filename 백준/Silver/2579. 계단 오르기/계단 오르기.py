import sys

input = sys.stdin.readline

def dp(): # 점화식: dp[i]=max(dp[i−2]+li[i],dp[i−3]+li[i−1]+li[i])
    if n == 1:
        print(li[0])
        return
    elif n == 2:
        print(li[0] + li[1])
        return

    sol_list = [0 for _ in range(n)]
    sol_list[0] = li[0]
    sol_list[1] = li[0] + li[1]
    sol_list[2] = max(li[0] + li[2], li[1] + li[2])

    for i in range(3, n):
        sol_list[i] = max(sol_list[i-2] + li[i], sol_list[i-3] + li[i-1] + li[i])

    print(sol_list[-1])


n = int(input())
li = [0 for _ in range(n)]
for i in range(n):
    li[i] = int(input())
dp()