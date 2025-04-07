import sys
from collections import defaultdict

input = sys.stdin.readline
n, m = map(int, input().split())

words_dic = defaultdict(int)
sorted_list = []

for _ in range(n):
    word = input().strip()
    if len(word) >= m:
        words_dic[word] += 1


# (빈도수, 길이, 원본 단어)로 구성된 튜플의 배열
arr = [(words_dic[i], len(i), i) for i in words_dic]
# 1. 빈도수 역순 / 2. 단어 길이 역순 / 3. 원본 단어 사전순 정렬
arr.sort(key=lambda x: (-x[0], -x[1], x[2]))

for i in arr:
    print(i[2])