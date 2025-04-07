x = 1
y = 1
g = 0
h = 0
count = 1
n = int(input())

while count < n:
    if n == 1:
        break

    if x == 1 and y % 2 == 0 and n - count >= y:
        count += y-1
        x = y
        y = 1

    elif x == 1 and y % 2 == 0 and not n - count >= y:
        h = y
        for i in range(h-1):
            if count == n:
                break
            x += 1
            y -= 1
            count += 1

    elif x == 1 and y % 2 != 0:
        y += 1
        count += 1

    elif x % 2 == 0 and y == 1:
        x += 1
        count += 1

    elif x % 2 != 0 and y == 1 and n - count >= x:
        count += x-1
        y = x
        x = 1

    elif x % 2 != 0 and y == 1 and not n - count >= x:
        g = x
        for i in range(g-1):
            if count == n:
                break
            x -= 1
            y += 1
            count += 1
        continue

print(f"{x}/{y}")