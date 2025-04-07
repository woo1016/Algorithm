import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
set_nums = set(nums)
length = len(set_nums)
again_nums = list(set_nums)
again_nums.sort()

dic = {}

for i in range(len(again_nums)):
    dic[again_nums[i]] = i

for i in range(len(nums)):
    print(dic[nums[i]], end=" ")