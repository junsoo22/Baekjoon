

for tc in range(10):
    N = int(input())
    code = list(map(int, input().split()))
    order_num = int(input())
    order = input().split()

    idx = 0
    while idx < len(order):
        if order[idx] == 'I':
            x = int(order[idx + 1])
            y = int(order[idx + 2])
            s = list(map(int, order[idx + 3:idx + 3 + y]))
            code[x:x] = s
            idx += y + 3
        elif order[idx] == 'D':
            x = int(order[idx + 1])
            y = int(order[idx + 2])

            del code[x:x+y]
            idx += 3
        elif order[idx] == 'A':
            y = int(order[idx + 1])
            s = list(map(int, order[idx + 2: idx + 2 + y]))
            code[-1:-1] = s
            idx += y + 2

    print(f"#{tc+1} ", *code[:10])

