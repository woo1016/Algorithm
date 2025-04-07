import sys

input = sys.stdin.readline

# def fib(n):
#     global fib_count
#     if n ==1 or n == 2:
#         fib_count += 1
#         return 1
#     return fib(n-1) + fib(n-2)


def fibonacci(n):
    global  fibonacci_count
    f = [0] * (n+1)
    f[0] = 0
    f[1] = 1
    f[2] = 1

    for i in range(3, n+1):
        f[i] = f[i-1] + f[i-2]
        fibonacci_count += 1
    return f[n]


fib_count = fibonacci_count = 0
n = int(input())

kk = fibonacci(n)

print(kk, fibonacci_count)