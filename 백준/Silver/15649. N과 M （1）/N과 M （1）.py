import sys
input = sys.stdin.readline

def back(level):
    if len(solution_list) == len(set(solution_list)):
        if level == m:
            output_solution = ' '.join(map(str, solution_list))
            print(output_solution)
            return

        else: #해답 x 유망 o
            for i in range(1, n+1):
                if not i in solution_list:
                    if len(solution_list) < m:
                        solution_list.append(i)
                        back(level+1)
                        solution_list.pop()


n, m = map(int, input().split())

n_list = [i+1 for i in range(n)]
solution_list = []

back(0)