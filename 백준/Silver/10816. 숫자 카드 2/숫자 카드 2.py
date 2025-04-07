import sys
input = sys.stdin.readline


n = int(input())
nnum = list(map(int, input().split()))
n_list = [0]*20000002

for ele in nnum:
    n_list[ele-1] += 1

m = int(input())
mnum = list(map(int, input().split()))

for ele in mnum:
    print(n_list[ele-1], end=' ')