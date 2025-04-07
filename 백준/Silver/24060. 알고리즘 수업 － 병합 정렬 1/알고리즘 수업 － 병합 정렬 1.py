import sys
from collections import deque

input = sys.stdin.readline
count = 0
result = 0

def merge_sort_DC(li, low, high):
    mid = 0
    if low < high:
        mid = (low + high) // 2
        merge_sort_DC(li, low, mid)
        merge_sort_DC(li, mid + 1, high)
        merge(li, low, mid, high)


def merge(li, low, mid, high):
    global count, result

    n1 = low
    n2 = mid + 1
    s = low
    sortd = deque()#[0] * len(li)

    while n1 <= mid and n2 <= high:
        if li[n1] <= li[n2]:
            sortd.append(li[n1])
            s += 1
            n1 += 1
        else:
            sortd.append(li[n2])
            s += 1
            n2 += 1

    if n1 > mid:
        while n2 <= high:
            sortd.append(li[n2])
            s += 1
            n2 += 1

    else:
        while n1 <= mid:
            sortd.append(li[n1])
            s += 1
            n1 += 1

    for i in range(low, high + 1):
        li[i] = sortd.popleft()

        count += 1
        if count == k:
            result = li[i]


n, k = map(int, input().split())
a = list(map(int, input().split()))
merge_sort_DC(a, 0, len(a)-1)

if result != 0:
    print(result)
else:
    print(-1)