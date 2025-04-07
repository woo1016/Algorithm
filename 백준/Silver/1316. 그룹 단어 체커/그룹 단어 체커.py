n = int(input())
count = 0

for i in range(n):
    dan = input()
    bol = True
    a = []

    for j in range(len(dan)):
        if j == 0:
            a.append(dan[j])
            continue

        if dan[j] != dan[j-1] and dan[j] in a:
            bol = False
            break
        elif dan[j] != dan[j-1] and not (dan[j] in a):
            a.append(dan[j])

    if bol:
        count += 1

print(count)