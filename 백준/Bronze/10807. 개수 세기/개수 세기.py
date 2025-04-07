import sys

n = int(input())
nums = map(int, input().split())
v = int(input())
nums = list(nums)

k = 0
for i in range(n):
    if nums[i] == v:
        k+=1

print(k)