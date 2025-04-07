import sys
input = sys.stdin.readline

n = int(input())
ns = str(n)
nn = []
for i in range(len(ns)):
    nn.append(int(ns[i]))

nn.sort(reverse=True)
for i in range(len(nn)):
    print(nn[i], end='')