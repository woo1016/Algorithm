n, b = map(int, input().split())
remain_li = []
count = 0
i=0

while True:
    remain_li.append(n % b)
    n //= b

    if 9 < remain_li[i] < 36:
        remain_li[i] += 55
        remain_li[i] = chr(remain_li[i])

    if count == 1:
        break
    if n // b <= 0:
        count += 1

    i+=1

if remain_li[-1] == 0:
    remain_li.pop()

for i in range(len(remain_li)):
    print(remain_li[len(remain_li)-1-i], end="")