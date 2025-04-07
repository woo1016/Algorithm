import sys
input = sys.stdin.readline

n, m = map(int, input().split())
not_see = set()
not_listen = set()

for i in range(n):
    not_listen.add(input().strip())

for j in range(m):
    not_see.add(input().strip())

not_see_listen = not_see & not_listen
not_see_listen = list(not_see_listen)
not_see_listen.sort()

print(len(not_see_listen))
print("\n".join(map(str, not_see_listen)))