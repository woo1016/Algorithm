import sys
from functools import reduce
import math

input = sys.stdin.readline

n = int(input())
sosu_list = []

for i in range(n):
    test_case = int(input())

    while True:
        sosu = True

        if test_case < 2:
            sosu = False
            
        sqrt_test_case = int(math.sqrt(test_case))

        for i in range(2, sqrt_test_case + 1):
            if test_case % i == 0:
                sosu = False
                break

        if not sosu:
            test_case += 1
        else:
            break
    print(test_case)