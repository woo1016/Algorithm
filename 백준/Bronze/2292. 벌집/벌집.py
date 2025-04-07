n = int(input())

i = 0
fi = 2

while n != 1:
    k = fi + (6 * i)
    kk = k + (6 * (i + 1) - 1)
    fi = k
    if k <= n <= kk:
        i += 1
        break
    i += 1

# if 2 <= n <= 7: # 7-2 = 5
#     i = 2
# elif 8 <= n <= 19: # 19-8 = 11
#     i = 3
# elif 20 <= n <= 37: # 37-20 = 17
#     i = 4
# elif 38 <= n <= 61: # 61-38 = 23
#     i = 5
# elif 62 <= n <= 70: # 70-62 = 8
#     i += 6
i += 1
print(i)