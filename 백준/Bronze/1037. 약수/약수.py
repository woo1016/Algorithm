import sys

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))

print(max(arr)*min(arr))

# 진짜 약수들 중에서 최소값과 최대값을 곱하면 
# 𝑁
# N을 구할 수 있는 이유는, 모든 약수들이 짝을 이루기 때문입니다. 그 중 가장 작은 값과 가장 큰 값이 곱해져서 
# 𝑁
# N이 되며, 중간의 약수들은 이 두 값의 곱을 이용해 구성됩니다.