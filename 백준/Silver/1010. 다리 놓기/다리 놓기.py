import sys

input = sys.stdin.readline


def factorial(a):
    if a == 0:
        return 1
    return a * factorial(a - 1)


for i in range(int(input())):
    n, m = map(int, input().split())
    n_fact = factorial(n)
    m_fact = factorial(m)
    m_n_fact = factorial(m-n)
    print(int(m_fact / (n_fact * m_n_fact)))
