import sys

input = sys.stdin.readline
rainbow_dance = set()
rainbow_dance.add("ChongChong")

for i in range(int(input())):
    a, b = input().strip().split()
    if a in rainbow_dance and not (b in rainbow_dance):
        rainbow_dance.add(b)

    elif b in rainbow_dance and not (a in rainbow_dance):
        rainbow_dance.add(a)

print(len(rainbow_dance))