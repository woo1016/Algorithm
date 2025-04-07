a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())
bol = True

for i in range(n0, 101):
    fn = (a1 * i) + a0
    gn = i * c
    if fn > gn:
        bol = False
        break

if bol:
    print(1)
else:
    print(0)
