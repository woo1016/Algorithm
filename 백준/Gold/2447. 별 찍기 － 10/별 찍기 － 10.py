import sys

input = sys.stdin.readline

#분할정복 기법 필요
def draw_star(n):
    if n == 1:
        return ["*"]

    sub_pattern = draw_star(n // 3)  # 1/3 크기의 패턴 생성
    stars = []

    for i in range(3):
        for line in sub_pattern:
            if i == 1:  # 가운데 줄일 때
                stars.append(line + " " * (n // 3) + line)
            else:
                stars.append(line * 3)

    return stars


n = int(input())  # 입력값 (N은 항상 3^k 형태)
result = draw_star(n)
print("\n".join(result))