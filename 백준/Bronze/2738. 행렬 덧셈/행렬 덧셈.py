n, m = map(int, input().split())
a = []
b = []
c = []

for i in range(n):
    a.append(list(map(int, input().split())))

for i in range(n):
    b.append(list(map(int, input().split())))

for i in range(n):
    c.append([])
    for j in range(m):
        c[i].append(a[i][j] + b[i][j])
        print(c[i][j], end=" ")
    print()
