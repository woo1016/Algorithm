n = 9
a = []
mx = 0
mx_r = 0
mx_l = 0

for i in range(n):
    a.append(list(map(int, input().split())))
    for j in range(len(a[i])):
        if mx < a[i][j]:
            mx = a[i][j]
            mx_r = i
            mx_l = j

print(mx)
print(mx_r+1, mx_l+1)