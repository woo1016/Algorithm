a, b, v = map(int, input().split())

c = a - b # 일일 m
r = v - a # n-1의 상황
result = 0

if r > 0:

    if r < c:
        result = 1
    else:
        result = r // c
        if r % c != 0:
            result += 1

result += 1
print(result)