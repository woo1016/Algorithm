import sys

input = sys.stdin.readline

def su():
    dp = [0 for _ in range(n)]
    if n == 1:
        print(1)
        return

    elif n == 2:
        if a[0] < a[1]:
            print(2)
            return
        else:
            print(1)
            return
    if a[1] > a[0]:
        dp[0] = 1
        dp[1] = 2
    else:
        dp[1] = 1

    for i in range(2, n):
        mx = 0
        for j in range(i):
            if a[j] < a[i]:
                if mx < dp[j]:
                    mx = dp[j]

        if a[i] > a[i-1]:
            dp[i] = max(dp[i-1] + 1, mx + 1)
        else:
            dp[i] = mx + 1

    print(max(dp))


n = int(input())
a = list(map(int, input().split()))
su()