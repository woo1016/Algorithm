import sys
import math
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    a, b = map(int, input().split())
    a_set = set()
    b_set = set()
    mx = 0
    least_common_multiple = 0

    for i in range(2, min(a, b)+1):
        if a%i == 0:
            a_set.add(i)
        else:
            continue

        if b%i == 0:
            b_set.add(i)

    if a_set & b_set:
        mx = max(a_set & b_set)
        least_common_multiple = b * (a // mx)
    else:
        least_common_multiple = a * b
    print(least_common_multiple)