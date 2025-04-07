import sys
input = sys.stdin.readline

n = int(input())
enter_person = set()

for i in range(n):
    name, status = input().split()
    if status == 'leave' and name in enter_person:
        enter_person.remove(name)
    if status == 'enter':
        enter_person.add(name)

enter_person = list(enter_person)
enter_person.sort(reverse=True)

for i in range(len(enter_person)):
    print(enter_person[i])