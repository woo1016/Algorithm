a1, b1 = map(int, input().split())
a2, b2 = map(int, input().split())
a3, b3 = map(int, input().split())

a4 = a1
b4 = b1

if a4 == a2:
    a4 = a3
elif a4 != a2:
    if a4 == a3:
        a4 = a2

if b4 == b2:
    b4 = b3
elif b4 != b2:
    if b4 == b3:
        b4 = b2
print(a4, b4)