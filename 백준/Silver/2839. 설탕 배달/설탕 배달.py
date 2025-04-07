n = int(input())
counts = []
mn = 1000000
aa = n // 5

while aa >= 0:
    bb = 0
    nn = n - (5 * aa)
    while bb <= nn//3:

        count = 0
        k = nn - (3 * bb)
        if k == 0:
            if mn > aa + bb:
                mn = aa + bb
        bb += 1
    aa -= 1

if mn == 1000000:
    print(-1)
else:
    print(mn)