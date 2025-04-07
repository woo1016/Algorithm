import sys

input = sys.stdin.readline

def tile():
    solution[1] = 1
    solution[2] = 2

    for i in range(3, n+1):
        solution[i] = solution[i-1] + solution[i-2]
        solution[i] %= 15746


n = int(input())
if n <= 2:
    print(n)

else:
    solution = [0] * (n + 1)
    tile()
    print(solution[n])