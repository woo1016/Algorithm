import random
import time
import sys
import copy

sys.setrecursionlimit(10 ** 9)  # 재귀 한계 올리기


# 알고리즘 합병 정렬과 퀵 정렬을 구현하고 데이터 크기에 따른 실행 시간을 측정한다.
# 여러 데이터 크기와 각 데이터 크기에 대하여 서로 다른 데이터를 여러 번 무작위로 생성하면서 실험하기 위해
# 중첩 for문을 이용하여 입력 받은 정수 크기만큼의 데이터(리스트)를 여러 번 랜덤으로 생성했다.
# 생성된 데이터는 합병 정렬과 퀵 정렬에 사용된다.
# 합병 정렬은 merge_sort_DC 함수와 merge 함수로 구현했고
# 퀵 정렬은 quicksort 함수와 partiton 함수로 구현했다.
def merge_sort_DC(bl: list, low: int, high: int):
    # 합병정렬 분할
    li = []
    if low < high:  # 부문제의 크기가 2 이상
        middle = int((low + high) / 2)  # 리스트의 중앙 인덱스
        # 분할
        low_li = bl[:middle]  # 인덱스 0부터 중앙-1 인덱스까지
        mihi_li = bl[middle:]  # 중앙 인덱스부터 마지막 인덱스까지
        if len(bl) >= 2:  # 리스트 길이가 2 이상
            low_li = merge_sort_DC(low_li, 0, len(low_li))  # 왼쪽 원소들 분할
            mihi_li = merge_sort_DC(mihi_li, 0, len(mihi_li))  # 오른쪽 원소들 분할
        # 정복된 하위 리스트(부문제)를 병합하여 정렬 결과를 얻음
        # 분할된 두 리스트를 합쳐서 병합.
        merged = merge(low_li + mihi_li, 0, len(low_li), len(low_li) + len(mihi_li))
        bl = merged
        li = bl
    return li


def merge(li: list, low: int, mid: int, high: int):
    n1 = low
    n2 = mid
    s = 0
    sorted_list = [0] * (high - low)  # 합병되는 원소 저장할 리스트
    # i: int
    if len(li) == 2:  # 원소가 2개 남은 경우
        if li[0] <= li[1]:
            sorted_list[0] = li[0]
            sorted_list[1] = li[1]
        else:
            sorted_list[0] = li[1]
            sorted_list[1] = li[0]
    else:
        while n1 < mid and n2 < high:
            # 왼쪽 부문제는 중앙 인덱스 - 1까지, 오른쪽 부문제는 중앙 인덱스부터 마지막 인덱스까지
            if li[n1] <= li[n2]:
                sorted_list[s] = li[n1]
                n1 += 1
                s += 1
            else:
                sorted_list[s] = li[n2]
                n2 += 1
                s += 1
        if n1 >= mid:
            # 1번째 그룹이 전패 했을 경우
            while n2 < high:
                sorted_list[s] = li[n2]
                s += 1
                n2 += 1
        else:
            # 2번째 그룹이 전패 했을 경우
            while n1 < mid:
                sorted_list[s] = li[n1]
                s += 1
                n1 += 1
    for i in range(low, high):
        # print(f"i: {i}")
        li[i] = sorted_list[i - low]
    return li


def partition(bl: list, low: int, high: int):
    j = low
    cmp = 0
    for i in range(low + 1, high):  # 리스트 순회하며 피봇과 비교
        if bl[i] < bl[low]:
            j += 1  # 피봇보다 작은 데이터들의 마지막 위치
            # j번째와 i번째 데이터 교환
            cmp = bl[j]
            bl[j] = bl[i]
            bl[i] = cmp
    # 마지막으로 피봇과 j번째 데이터 교환
    cmp = bl[low]
    bl[low] = bl[j]
    bl[j] = cmp
    return j  # 최종 변경된 피봇의 위치


def quicksort(bl: list, low: int, high: int):
    # 퀵정렬
    if low < high:
        pivot_pos = partition(bl, low, high)  # 피봇 이동
        # 위치가 정해진 피봇을 제외하고 분할
        quicksort(bl, low, pivot_pos - 1)  # 피봇보다 작았던 데이터 집합 분할
        quicksort(bl, pivot_pos + 1, high)  # 피봇보다 큰 데이터 집합 분할
    return bl


for i in range(0, 5):
    print(f"\n{i + 1} 번째 입니다.\n")
    n = int(input("데이터 개수 입력: "))
    for j in range(0, 5):  # 서로 다른 데이터 무작위 생성해서 여러 번 실험
        beginning_list = [random.randrange(0, 1000000) for _ in range(n)]  # 난수 리스트 생성
        beginning_list2 = copy.deepcopy(beginning_list)

        merge_start = time.time()  # 합병정렬 시간 측정 시작
        merge_list = merge_sort_DC(beginning_list, 0, len(beginning_list))  # 합병정렬
        merge_end = time.time()  # 측정 끝

        print(f'시도 {j + 1}')

        print(f"합병정렬 {merge_end - merge_start:.5f} sec")
        merge_list.clear()
        merge_time = merge_end - merge_start

        quick_start = time.time()  # 퀵정렬 시간 측정 시작
        quick_list = quicksort(beginning_list2, 0, len(beginning_list))  # 퀵정렬
        quick_end = time.time()  # 측정 끝
        quick_time = quick_end - quick_start
        print(f"퀵정렬 {quick_time:.5f} sec\n")
