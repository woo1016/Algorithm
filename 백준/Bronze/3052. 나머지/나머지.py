li = [0]*10
n = []

for i in range(10):
    li[i] = int(input())%42

n.append(li[0])
for i in range(1, 10):
    c = 0
    for j in range(len(n)):
        if li[i] == n[j]:
            c += 1
    if c == 0:
        n.append(li[i])

print(len(n))