import sys

input = sys.stdin.readline
def su():
    dp = [0 for _ in range(n)]

    for i in range(n):
        dp[i] = 1
        for j in range(i):
            if a[i][1] > a[j][1]:
                dp[i] = max(dp[i], dp[j] + 1)

    print(n - max(dp))


n = int(input())
a = []
for i in range(n):
    a.append(tuple(map(int, input().split())))

a.sort()
su()
