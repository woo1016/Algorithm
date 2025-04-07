import sys

input = sys.stdin.readline

def su():
    llis = [0 for _ in range(n)]
    rlis = [0 for _ in range(n)]
    mx = 0

    for i in range(n):
        llis[i] = 1
        for j in range(i):
            if a[i] > a[j]:
                llis[i] = max(llis[i], llis[j] + 1)

    for i in range(n-1, -1, -1):
        rlis[i] = 1
        for j in range(n-1, i, -1):
            if a[i] > a[j]:
                rlis[i] = max(rlis[i], rlis[j] + 1)

    for i in range(n):
        mx = max(mx, llis[i] + rlis[i])
    print(mx-1)


n = int(input())
a = list(map(int, input().split()))
su()