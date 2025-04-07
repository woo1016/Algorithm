import sys

input = sys.stdin.readline

def dp(n):
    solution = [0] * n
    if n == 1:
        print(sake[0])
        return
    elif n == 2:
        print(sake[0] + sake[1])
        return

    solution[0] = sake[0]
    solution[1] = sake[0] + sake[1]
    solution[2] = max(sake[0] + sake[1], sake[0] + sake[2], sake[1] + sake[2])

    for i in range(3, n):
        solution[i] = max(solution[i-1], solution[i-2] + sake[i], solution[i-3] + sake[i-1] + sake[i])

    print(solution[-1])


n = int(input())
sake = []
for i in range(n):
    sake.append(int(input()))

dp(n)