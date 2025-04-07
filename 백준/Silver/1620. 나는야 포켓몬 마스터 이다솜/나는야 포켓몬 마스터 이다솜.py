import sys
# input = sys.stdin.readline

n, m = map(int, sys.stdin.readline().strip().split())
name_dogam = {}
num_dogam = {}
li = []

for i in range(n):
    inp = input()
    name_dogam[i+1] = inp
    num_dogam[inp] = i+1

for i in range(m):
    inp = input()

    if inp.isdigit():
        li.append(name_dogam[int(inp)])
    else:
        li.append(num_dogam[inp])

for ele in li:
    print(ele)