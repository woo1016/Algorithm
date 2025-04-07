n = int(input())
a = list(map(int, input().split()))

mn = mx = a[0]

for i in range(n):
    if a[i] < mn:
        mn = a[i]
    if a[i] > mx:
        mx = a[i]
print(mn, mx)