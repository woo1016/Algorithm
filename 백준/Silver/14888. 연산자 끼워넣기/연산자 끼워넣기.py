import sys

input = sys.stdin.readline

def back(level):
    global result
    if level == n:
        sol_list.append(result)
        return

    if operators[0] > 0:
        temp = result
        result += a[level]
        operators[0] -= 1
        back(level+1)
        operators[0] += 1
        result = temp

    if operators[1] > 0:
        temp = result
        result -= a[level]
        operators[1] -= 1
        back(level+1)
        operators[1] += 1
        result = temp

    if operators[2] > 0:
        temp = result
        result *= a[level]
        operators[2] -= 1
        back(level+1)
        operators[2] += 1
        result = temp

    if operators[3] > 0:
        temp = result
        if result < 0 < a[level]: # 음수를 양수로 나눌 때
            result = abs(result)
            result //= a[level]
            result = -result
        else:
            result //= a[level]

        operators[3] -= 1
        back(level+1)
        operators[3] += 1
        result = temp


n = int(input())
a = list(map(int, input().split()))
operators = list(map(int, input().split()))
sol_list = []
result = a[0]

back(1)
mx = max(sol_list)
mn = min(sol_list)
print(mx)
print(mn)