li = [0]*30
no = []
for i in range(28):
    j = int(input())
    li[j-1] = 1

for i in range(30):
    if li[i] == 0:
        no.append(i)

if no[0] >= no[1]:
    cmp = no[0]
    no[0] = no[1]
    no[1] = cmp

print(no[0]+1)
print(no[1]+1)