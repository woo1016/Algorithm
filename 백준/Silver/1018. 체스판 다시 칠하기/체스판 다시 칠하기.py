n, m =map(int, input().split())
maps = []
li = []
for i in range(n):
    maps.append(list(input()))

for i in range(len(maps)-7):
    for j in range(len(maps[i])-7):
        gizon = maps[i][j]
        for u in range(2):
            count = 0
            cmp_list = [[], [], [], [], [], [], [], []]
            m = 0
            for k in range(i, i+8):
                for l in range(j, j+8):
                    cmp_list[m].append(maps[k][l])
                m += 1

            for a in range(len(cmp_list)):
                for b in range(len(cmp_list[0])):
                    if gizon == 'W':
                        if a % 2 == 0:
                            if b % 2 == 0:
                                if cmp_list[a][b] != 'W':
                                    count += 1
                            elif b % 2 != 0:
                                if cmp_list[a][b] != 'B':
                                    count += 1
                        elif a % 2 != 0:
                            if b % 2 == 0:
                                if cmp_list[a][b] != 'B':
                                    count += 1
                            elif b % 2 != 0:
                                if cmp_list[a][b] != 'W':
                                    count += 1

                    elif gizon == 'B':
                        if a % 2 == 0:
                            if b % 2 == 0:
                                if cmp_list[a][b] != 'B':
                                    count += 1
                            elif b % 2 != 0:
                                if cmp_list[a][b] != 'W':
                                    count += 1
                        elif a % 2 != 0:
                            if b % 2 == 0:
                                if cmp_list[a][b] != 'W':
                                    count += 1
                            elif b % 2 != 0:
                                if cmp_list[a][b] != 'B':
                                    count += 1
            if gizon == 'W':
                gizon = 'B'
            elif gizon == 'B':
                gizon = 'W'
            li.append(count)

#        maps[i][j] = gizon

print(min(li))