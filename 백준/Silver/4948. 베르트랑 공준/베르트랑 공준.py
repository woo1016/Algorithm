import sys
from functools import reduce
import math

input = sys.stdin.readline
inputs = []
n = int(input())

while n != 0:
    inputs.append(n)
    n = int(input())

max_num = max(inputs) * 2


def calculate(max_num):
    is_prime = [True] * (max_num + 1)
    is_prime[0] = is_prime[1] = False
    for current in range(2, int(max_num ** 0.5) + 1):
        if is_prime[current]:
            for mult in range(current * current, max_num + 1, current):
                is_prime[mult] = False
    return is_prime


is_prime = calculate(max_num)
prefix_num = []
pre_count = 0
for i in range(max_num + 1):
    if is_prime[i]:
        pre_count += 1
    prefix_num.append(pre_count)

for num in inputs:
    result = prefix_num[2*num] - prefix_num[num]
    print(result)