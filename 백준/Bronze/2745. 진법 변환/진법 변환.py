n, b = input().split()
n = list(n)
b = int(b)
result = 0
j = 0

for i in range(len(n)-1, -1, -1):
    if 64 < int(ord(n[i])) < 91:
        n[i] = int(ord(n[i]))
        n[i] -= 55
    else:
        n[i] = int(n[i])
    n[i] *= b**j

    result += n[i]
    j+=1
print(result)