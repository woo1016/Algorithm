n, m = map(int, input().split())
li = [0]*n

for mmm in range(m):
    i, j, k = map(int, input().split())
    i -= 1
    while i != j:
        li[i] = k
        i+=1

for i in range(n):
    print(li[i], end=" ")