a = int(input())
b = int(input())
c = int(input())

if a == b and b == c and c == a and a == 60:
    print("Equilateral")
elif a + b + c == 180:
    if a == b or b == c or c == a:
        print("Isosceles")
    elif a!= b or b!= c or c!=a:
        print("Scalene")
else:
    print("Error")