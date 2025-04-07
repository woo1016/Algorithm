while True:
    a, b, c = map(int, input().split())
    if a == b == c == 0:
        break
    mx = a
    if mx < b:
        mx = b
    if mx < c:
        mx = c

    if mx == a:
        if mx >= b + c:
            print("Invalid")
            continue
    elif mx == b:
        if mx >= a + c:
            print("Invalid")
            continue
    elif mx == c:
        if mx >= a + b:
            print("Invalid")
            continue

    if a == b == c:
        print("Equilateral")
    elif (a == b and b != c) or (b == c and a != c)\
            or (a ==c and b != c):
        print("Isosceles")
    elif a != b != c:
        print("Scalene")