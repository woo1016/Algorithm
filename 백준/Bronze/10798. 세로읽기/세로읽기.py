dan_lists = []

for i in range(5):
    dan_list = list(input())
    while len(dan_list) < 15:
        dan_list.append("")
    dan_lists.append(dan_list)

for j in range(15):
    for i in range(5):
        if dan_lists[i][j] != "":
            print(dan_lists[i][j], end="")