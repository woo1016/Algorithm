n = int(input())
an = map(int, input().split())
an = list(an)
m = max(an)
result = 0

for i in range(n):
    an[i] = an[i]/m*100
    result += an[i]

result /= n
print(result)