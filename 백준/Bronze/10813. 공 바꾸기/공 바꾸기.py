n, m = map(int, input().split())
li = [0]*n
for i in range(n):
    li[i] = i+1

for k in range(m):
    i, j = map(int, input().split())
    i -= 1
    j -= 1
    cmp = li[i]
    li[i] = li[j]
    li[j] = cmp

for i in range(n):
    print(li[i], end=" ")