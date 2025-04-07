import sys

#input = sys.stdin.readline

while True:
    ps = list(input())
    bol = True
    left = []
    if len(ps) == 0:
        print("yes")

    elif ps[0] == '.' and len(ps) == 1:
        break

    elif ps[-1] == '.':
        for j in range(len(ps)):
            if ps[j] == '(' or ps[j] == '[':
                left.append(ps[j])
            elif (ps[j] == ')' or ps[j] == ']') and len(left) == 0:
                bol = False
                break

            elif len(left):
                if (left[-1] == '(' and ps[j] == ']') or \
                        (left[-1] == '[' and ps[j] == ')'):
                    bol = False
                    break

                elif left[-1] == '(' and ps[j] == ')':
                    left.pop()
                elif left[-1] == '[' and ps[j] == ']':
                    left.pop()

        if bol and len(left) == 0:
            print("yes")
        else:
            print("no")