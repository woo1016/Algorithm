import sys
input = sys.stdin.readline

arr = input().strip()
count = 0
sets = set()

for i in range(len(arr)):
    for j in range(i, len(arr)):
        sets.add(arr[i:j+1])

print(len(sets))