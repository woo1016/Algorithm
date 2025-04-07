sp = input()
sp2 = []
counts = [0]*26

for i in range(len(sp)):
    ord_sp = ord(sp[i])
    if ord_sp >= ord('a') and ord_sp <= ord('z'):
        ord_sp = ord_sp - 32

    sp2.append(ord_sp)
    counts[ord_sp-65] += 1

mx = 0
am = 0
bol = False
for i in range(len(counts)):
    if mx <= counts[i]:
        mx = counts[i]
        am = i

for i in range(am):
    if mx == counts[i]:
        bol = True
        break

if bol:
    mx = '?'
else:
    mx = am + 65
    mx = chr(mx)

print(mx)