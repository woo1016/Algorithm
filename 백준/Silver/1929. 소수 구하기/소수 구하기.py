import sys
from functools import reduce
import math

input = sys.stdin.readline

m, n = map(int, input().split())

for i in range(m, n+1):
    test_case = i
    sosu = True

    if test_case < 2:
        sosu = False

    sqrt_test_case = int(math.sqrt(test_case))

    for j in range(2, sqrt_test_case + 1):
        if test_case % j == 0:
            sosu = False
            break

    if sosu:
        print(test_case)