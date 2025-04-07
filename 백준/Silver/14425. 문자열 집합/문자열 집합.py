n, m = map(int, input().split())
s = set()
count = 0

for i in range(n):
    s.add(input())

for i in range(m):
    st = input()
    if st in s:
        count += 1

print(count)
