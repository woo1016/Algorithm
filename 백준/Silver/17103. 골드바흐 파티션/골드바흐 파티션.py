import sys

input = sys.stdin.readline
inputs = []
n = int(input())
nums = []

for i in range(n):
    inputs.append(int(input()))

max_num = max(inputs)


def calculate(max_num):
    is_prime = [True] * (max_num + 1)
    is_prime[0] = is_prime[1] = False
    for current in range(2, int(max_num) + 1):
        if is_prime[current]:
            for mult in range(current * current, max_num + 1, current):
                is_prime[mult] = False
            nums.append(current) # 소수 배열
    return is_prime


is_prime = calculate(max_num)

for ele in inputs:
    pre_count = 0
    m = 0

    for j in range(len(nums)):
        if nums[j] > ele//2:
            break
        #if ele - nums[j] in nums: #이거를
        if is_prime[ele - nums[j]]: #이거로 바꾸니까 시간이 확 변하넹
            pre_count += 1

    print(pre_count)