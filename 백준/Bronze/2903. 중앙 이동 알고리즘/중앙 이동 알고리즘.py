x = 2
y = 2
n = int(input())

for i in range(n):
    k = 0
    for j in range(1, x, 1):
        k += 1
    x += k
    y += k
print(x*y)