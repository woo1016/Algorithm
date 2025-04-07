import sys

input = sys.stdin.readline

def dp(x):
    mod = 1000000000

    sol = [[0 for _ in range(10)] for _ in range(x)]

    for i in range(1, 10):
        sol[0][i] = 1

    for i in range(1, x):
        for j in range(10):
            if j == 0:
                sol[i][j] = sol[i - 1][1] % mod

            elif j == 9:
                sol[i][j] = sol[i-1][8] % mod

            else:
                sol[i][j] = (sol[i - 1][j - 1] + sol[i - 1][j + 1]) % mod
    print(sum(sol[n-1]) % mod)


n = int(input())
dp(n)