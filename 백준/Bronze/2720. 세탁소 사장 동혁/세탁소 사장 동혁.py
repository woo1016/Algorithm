t = int(input())
quarter = 25
dime = 10
nickel = 5
penny = 1

for i in range(t):
    c = int(input())
    count_list = [0, 0, 0, 0]
    
    while c >= 1:
        if  c >= quarter:
            c-= quarter
            count_list[0] += 1
            continue
        elif c >= dime:
            c-= dime
            count_list[1] += 1
            continue
        elif c >= nickel:
            c-= nickel
            count_list[2] += 1
            continue
        elif c >= penny:
            c-= penny
            count_list[3] += 1
            continue
    for j in range(4):
        print(count_list[j], end=" ")
    print()