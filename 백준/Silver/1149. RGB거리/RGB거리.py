import sys

input = sys.stdin.readline

def dp():

    sol = [[0, 0, 0] for _ in range(n)]

    sol[0][0] = cost_list[0][0]
    sol[0][1] = cost_list[0][1]
    sol[0][2] = cost_list[0][2]

    for i in range(1, n):
        sol[i][0] = min(cost_list[i][0] + sol[i-1][1], cost_list[i][0] + sol[i-1][2])
        sol[i][1] = min(cost_list[i][1] + sol[i - 1][0], cost_list[i][1] + sol[i - 1][2])
        sol[i][2] = min(cost_list[i][2] + sol[i - 1][0], cost_list[i][2] + sol[i - 1][1])

    print(min(sol[-1]))


n = int(input())
cost_list = []
for i in range(n):
    cost_list.append(list(map(int, input().split())))

dp()