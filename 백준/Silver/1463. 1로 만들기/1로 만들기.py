import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

def dp(x):
    a = b = c = 0
    if x in solution:
        return solution[x]

    if x == 1:
        return 0
    if x == 2 or x == 3:
        return 1

    if x % 3 == 0:
        a = dp(x // 3) + 1

    if x % 2 == 0:
        b = dp(x // 2) + 1

    c = dp(x - 1) + 1

    if a == 0 and b == 0:
        solution[x] = c

    elif a == 0:
        solution[x] = min(b, c)
    elif b == 0:
        solution[x] = min(a, c)

    else:
        solution[x] = min(a, b, c)
    return solution[x]


n = int(input())
solution = {}
result = dp(n)
print(result)