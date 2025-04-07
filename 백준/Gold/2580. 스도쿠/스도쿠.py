import sys
input = sys.stdin.readline

solution_list = []
zero_list = []
rows = [set() for _ in range(9)]
cols = [set() for _ in range(9)]
boxes = [set() for _ in range(9)]


for i in range(9):
    row = list(map(int, input().split()))
    solution_list.append(row)
    for j in range(9):
        if row[j] == 0:
            zero_list.append((i, j))
        else:
            num = row[j]
            rows[i].add(num)                           # 행 i에 num 추가
            cols[j].add(num)                           # 열 j에 num 추가
            boxes[(i // 3) * 3 + (j // 3)].add(num)      # 박스 인덱스 계산 후 num 추가

def back(level):
    if level == len(zero_list):

        for r in solution_list:
            print(' '.join(map(str, r)))
        sys.exit()

    r, c = zero_list[level]
    box_index = (r // 3) * 3 + (c // 3)
    for num in range(1, 10):

        if num not in rows[r] and num not in cols[c] and num not in boxes[box_index]:
            solution_list[r][c] = num
            rows[r].add(num)
            cols[c].add(num)
            boxes[box_index].add(num)

            back(level + 1)


            solution_list[r][c] = 0
            rows[r].remove(num)
            cols[c].remove(num)
            boxes[box_index].remove(num)

back(0)
