import sys

input = sys.stdin.readline


def cantor(low:int, high:int):
    if high - low < 1:
        return

    elif high - low == 2:
        arr[low+1] = ' '
        return

    center = (high - low + 1) // 3

    cantor(low, low + center - 1)
    arr[low + center:low + 2 * center] = [' '] * center
    cantor(low + 2 * center, high)


while True:
    try:
        n = input().strip()
        if not n:
            break
        n = int(n)
        nn = 3 ** n
        arr = ['-'] * nn
        cantor(0, len(arr) - 1)
        print(''.join(arr))
    except EOFError:
        break