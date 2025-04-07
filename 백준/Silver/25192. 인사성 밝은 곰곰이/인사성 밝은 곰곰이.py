import sys

input = sys.stdin.readline
arr = []
hello_person = set()
count = 0

for i in range(int(input())):
    arr.append(input().strip())

for i in range(len(arr)):
    if arr[i] == "ENTER":
        hello_person = set()

    elif not (arr[i] in hello_person):
        hello_person.add(arr[i])
        count += 1
print(count)