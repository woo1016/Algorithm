a, b, c = map(int, input().split())

if a == b == c:
    print(a + b + c)

else:
    while a + b <= c:
        c -= 1
    while b + c <= a:
        a -= 1
    while c + a <= b:
        b -= 1
    print(a + b + c)