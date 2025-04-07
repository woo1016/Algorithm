st = input()
croatia_count = 0
i = 0
j = 0

while i < len(st) and j < len(st):
    j = i + 1
    if i == len(st)-1 and j == len(st):
        croatia_count += 1
        break

    #print(f"i: {i}, j: {j}")
    if st[i] == "c":
        if st[j] == "=":
            croatia_count += 1
            i = j + 1
            continue
        elif st[j] == "-":
            croatia_count += 1
            i = j + 1
            continue
    if st[i] == "d":
        if st[j] == "z":
            if j+1 < len(st):
                if st[j + 1] == "=":
                    croatia_count += 1
                    i = j + 2
                    continue
        elif st[j] == "-":
            croatia_count += 1
            i = j + 1
            continue

    if st[i] == "l" and st[j] == "j":
        croatia_count += 1
        i = j + 1
        continue
    if st[i] == "n" and st[j] == "j":
        croatia_count += 1
        i = j + 1
        continue
    if st[i] == "s" and st[j] == "=":
        croatia_count += 1
        i = j + 1
        continue
    if st[i] == "z" and st[j] == "=":
        croatia_count += 1
        i = j + 1
        continue
    else:
        croatia_count += 1
        i += 1

print(croatia_count)