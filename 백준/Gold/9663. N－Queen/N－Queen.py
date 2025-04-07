import sys
input = sys.stdin.readline

def back(level):
    global result
    if level == n:
        result += 1
        return

    else: #해답 x 유망 o
        for i in range(n):
            bol = True
            for r in range(level):
                if solution_list[r] == i or abs(solution_list[r] - i) == level - r:
                    bol = False
                    break
            if bol:
                solution_list[level] = i
                back(level+1)


n = int(input())
solution_list = [0] * n
result = 0
back(0)
print(result)