def insertion(lis):
    sorted_list = [lis[0]]

    for i in range(1, len(lis)):
        for j in range(len(sorted_list)):
            if lis[i] < sorted_list[j]:
                sorted_list.insert(j, lis[i])
                break
            elif lis[i] > sorted_list[-1]:
                sorted_list.append(lis[i])
                break

    return sorted_list


n = int(input())
li = []
for i in range(n):
    li.append(int(input()))

sor_li = insertion(li)
for i in range(len(sor_li)):
    print(sor_li[i])
