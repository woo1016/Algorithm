import sys
input = sys.stdin.readline

def back(level):
        if level == m:
            output_solution = ' '.join(map(str, solution_list))
            print(output_solution)
            return

        else: #해답 x 유망 o
            for i in range(1, n+1):
                if len(solution_list) < m:
                    if len(solution_list) == 0:
                        solution_list.append(i)
                        back(level+1)
                        solution_list.pop()
                    elif len(solution_list) >= 1:
                        if solution_list[-1] <= i:
                            solution_list.append(i)
                            back(level + 1)
                            solution_list.pop()


n, m = map(int, input().split())

n_list = [i+1 for i in range(n)]
solution_list = []
back(0)