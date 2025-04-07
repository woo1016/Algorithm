import sys

input = sys.stdin.readline


def factorial(a):
    if a == 0:
        return 1
    return a * factorial(a - 1)


n, k = map(int, input().split())
n_fact = factorial(n)
k_fact = factorial(k)
n_k_fact = factorial(n-k)
print(int(n_fact / (k_fact * n_k_fact)))
