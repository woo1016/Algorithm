height = width = 100
square = height * [width *[0]]
location = []
n = int(input())

for k in range(n):
    y, x = map(int, input().split())
    y = 100 - y

    for i in range(10):
        for j in range(10):
            square[y-i][x+j] += 1
            if (y-i, x+j) not in location:
                location.append((y-i, x+j))
print(len(location))