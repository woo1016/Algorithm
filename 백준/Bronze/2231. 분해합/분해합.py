n = int(input())
bol = False
mini = 0

for ele in range(n, 0, -1):
    sang = 0
    c_ele = str(ele)
    for i in range(len(c_ele)):
        sang += int(c_ele[i])
    sang += ele
    if sang == n:
        bol = True
        mini = ele

if bol:
    print(mini)
else:
    print(0)