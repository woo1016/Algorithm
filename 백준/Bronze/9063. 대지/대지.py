n = int(input())
li = []
for i in range(n):
    li.append(list(map(int, input().split())))

mx_x = li[0][0]
min_x = li[0][0]
mx_y = li[0][1]
min_y = li[0][1]

for i in range(n):
    if mx_x < li[i][0]:
        mx_x = li[i][0]
    if min_x > li[i][0]:
        min_x = li[i][0]
    if mx_y < li[i][1]:
        mx_y = li[i][1]
    if min_y > li[i][1]:
        min_y = li[i][1]

result = (mx_x - min_x) * (mx_y - min_y)
print(result)