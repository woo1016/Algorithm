arr = []
score_obj_hap = 0
score_hap = 0
result = 0.0

for i in range(20):
    arr.append((input().split()))
    if arr[i][-1] == 'A+':
        arr[i][-1] = '4.5'
    elif arr[i][-1] == 'A0':
        arr[i][-1] = '4.0'
    elif arr[i][-1] == 'B+':
        arr[i][-1] = '3.5'
    elif arr[i][-1] == 'B0':
        arr[i][-1] = '3.0'
    elif arr[i][-1] == 'C+':
        arr[i][-1] = '2.5'
    elif arr[i][-1] == 'C0':
        arr[i][-1] = '2.0'
    elif arr[i][-1] == 'D+':
        arr[i][-1] = '1.5'
    elif arr[i][-1] == 'D0':
        arr[i][-1] = '1.0'
    elif arr[i][-1] == 'F':
        arr[i][-1] = '0.0'

    if arr[i][-1] != "P":
        score_obj_hap += float(arr[i][1]) * float(arr[i][-1])
        score_hap += float(arr[i][1])
result = score_obj_hap / score_hap
print(result)

