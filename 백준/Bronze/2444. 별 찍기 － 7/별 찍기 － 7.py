n = int(input())
nn = n * 2
u = 1

for i in range(nn-1):
    if i != 0:
        if i < n:
            u += 2
        else:
            u -= 2

    if i < n:
        for j in range(0, n-i-1):
            print(" ", end="")
    elif i >= n:
            for j in range(0, i-n+1):
                print(" ", end="")

    for uu in range(u):
        print("*", end="")
    print()



