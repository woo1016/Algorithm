sp = input()
yes = True
j = len(sp)-1

for i in range(len(sp)//2):
    if sp[i] != sp[j-i]:
        yes = False
        break

print(int(yes))
