a, b, c, d, e, f = map(int, input().split())
n = 0
m = 0
bol = False

for x in range(-999, 1000, 1):
    for y in range(-999, 1000, 1):
        if a * x + b * y == c and \
                d * x + e * y == f:
            bol = True
            n = x
            m = y
print(n, m)
