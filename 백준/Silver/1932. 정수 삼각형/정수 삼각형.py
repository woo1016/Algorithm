import sys

input = sys.stdin.readline

def dp():
    sol_list = [[0 for _ in range(n)] for _ in range(n)]
    sol_list[0][0] = li[0][0]

    for i in range(1, n):
        for j in range(len(li[i])):
            if j == 0: # 오른쪽 끝 원소의 경우
                sol_list[i][0] = li[i][0] + sol_list[i-1][0]
            elif j == len(li[i])-1: #왼쪽 끝 원소의 경우
                sol_list[i][j] = li[i][j] + sol_list[i-1][j-1]

            else: #위층 2개인 경우
                sol_list[i][j] = max(li[i][j] + sol_list[i-1][j-1], li[i][j] + sol_list[i-1][j])

    print(max(sol_list[-1]))


n = int(input())
li = []

for i in range(n):
    m = list(map(int, input().split()))
    li.append(m)

dp()