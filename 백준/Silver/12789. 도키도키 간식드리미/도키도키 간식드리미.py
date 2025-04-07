import sys

input = sys.stdin.readline

n = int(input())
student_list = list(map(int, input().split()))
student_list2 = student_list.copy()
standby_line = []
pas = 1
result_list = []

while pas <= n:
    if len(student_list) and student_list[0] == pas:
        pas += 1
        result_list.append(student_list.pop(0))

    elif len(standby_line) and standby_line[-1] == pas:
        pas += 1
        result_list.append(standby_line.pop(-1))

    elif (len(standby_line)) and (standby_line[-1] < student_list[0]):
        break
    else:
        standby_line.append(student_list.pop(0))

student_list2.sort()
if len(student_list2) == len(result_list):
    bol = True
    for i in range(n):
        if student_list2[i] != result_list[i]:
            bol = False
            break
    if bol:
        print('Nice')
else:
    print('Sad')
