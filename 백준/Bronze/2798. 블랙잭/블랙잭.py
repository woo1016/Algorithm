n, m = map(int, input().split())
li = list(map(int, input().split()))
result = 0

for i in range(len(li)):
    for j in range(len(li)):
        if i == j:
            continue
        for k in range(len(li)):
            if i == k or j == k:
                continue
            maybe = li[i] + li[j] + li[k]
            if result < maybe and maybe <= m:
                result = maybe
print(result)