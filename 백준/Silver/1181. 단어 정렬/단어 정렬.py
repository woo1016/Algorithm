import sys
#input = sys.stdin.readline

n = int(input())
li = []

for i in range(n):
    li.append(input())

result = set(li)
li = list(result)
li.sort(key=lambda x: (len(x), x))


for element in li:
    print(element)