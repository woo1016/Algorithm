import sys

input = sys.stdin.readline

arr = []
s = 0
dic = dict()
mx = 0
mode = 0

for i in range(int(input())):
    arr.append(int(input()))
    s += arr[i]
    if arr[i] in dic:
        dic[arr[i]] += 1
    else:
        dic[arr[i]] = 1
    mx = arr[i]

mx = max(dic.values())
keys = [k for k, v in dic.items() if v == mx]
keys.sort()
mode = keys[0]
if len(keys) >= 2:
    mode = keys[1]

average = s / len(arr)
average = round(average, 0)
arr.sort()
center = arr[len(arr)//2]
ran = max(arr) - min(arr)

print(int(average))
print(center)
print(mode)
print(ran)