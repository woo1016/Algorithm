li = []
average = 0

for i in range(5):
    li.append(int(input()))
    average += li[i]

average //= 5
li.sort()
print(average)
print(li[2])