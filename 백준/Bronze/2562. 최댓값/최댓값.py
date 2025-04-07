li = []
mx = 0
ii = 0
for i in range(9):
    li.append(int(input()))
    if li[i] > mx:
        mx = li[i]
        ii = i+1

print(mx)
print(ii)