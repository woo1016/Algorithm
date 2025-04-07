import sys

input = sys.stdin.readline

k = int(input())

for i in range(k):
    ps = list(input().strip())
    bol = True
    left = []

    for j in range(len(ps)):
        if ps[j] == '(':
            left.append('(')
        elif ps[j] == ')' and len(left) == 0:
            bol = False
            break
        elif ps[j] == ')' and len(left) > 0:
            left.pop()

    if bol and len(left) == 0:
        print("YES")
    else:
        print("NO")