n, m = map(int, input().split())
li = [i for i in range(1, n + 1)]

for k in range(m):
    i, j = map(int, input().split())
    i -= 1
    j -= 1

    while i <= j:
        cmp = li[i]
        li[i] = li[j]
        li[j] = cmp
        i+=1
        j-=1

for i in range(len(li)):
    print(li[i], end=" ")