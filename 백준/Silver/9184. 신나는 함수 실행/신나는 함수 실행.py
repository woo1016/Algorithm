import sys

input = sys.stdin.readline

def w_func():
    for i in range(21):
        for j in range(21):
            for u in range(21):
                if i == 0 or j == 0 or u == 0:
                     w[i][j][u] = 1

                elif i < j < u:
                    w[i][j][u] = w[i][j][u-1] + w[i][j-1][u-1] - w[i][j-1][u]
                else:
                    w[i][j][u] = w[i-1][j][u] + w[i-1][j-1][u] + w[i-1][j][u-1] - w[i-1][j-1][u-1]


w = [[[0]* 21 for _ in range(21)]for _ in range(21)]
w_func()


while True:
    a, b, c = map(int, input().strip().split())
    if a == b == c == -1:
        break

    result = 0


    if a <= 0 or b <= 0 or c <= 0:
        result = 1
    elif a > 20 or b > 20 or c > 20:
        result = w[20][20][20]
    else:
        result = w[a][b][c]

    print(f'w({a}, {b}, {c}) = {result}')