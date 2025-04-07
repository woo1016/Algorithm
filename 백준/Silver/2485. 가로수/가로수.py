import sys
from functools import reduce
import math

input = sys.stdin.readline

n = int(input())
li = []
k = []
for i in range(n):
    li.append(int(input()))
    if i >= 1:
        k.append(li[i] - li[i - 1])

mn = int(reduce(math.gcd, k))
total = 0

for i in range(len(k)):
    l = k[i] - mn
    total += l // mn

print(total)
