import sys

input = sys.stdin.readline

def back(level, start_score, link_score):
    global lank

    if level == n:
        if len(start) == n//2:
            lank = min(lank, abs(start_score - link_score))
        return


    if len(start) < n//2:
        new_start_score = start_score
        for k in start:
            new_start_score += s[level][k] + s[k][level]
        start.append(level)
        back(level+1, new_start_score, link_score)
        start.pop()

    if len(link) < n//2:
        new_link_score = link_score
        for k in link:
            new_link_score += s[level][k] + s[k][level]
        link.append(level)
        back(level+1, start_score, new_link_score)
        link.pop()


s = []
start = []
link = []
lank = 10000
count = 0
n = int(input())
for _ in range(n):
    s.append(list(map(int, input().split())))


back(0, 0, 0)
print(lank)