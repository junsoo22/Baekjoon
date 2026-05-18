

for tc in range(10):
    N = int(input())

    code = list(map(int, input().split()))
    order_num = int(input())
    order = input().split()

    idx=0
    for _ in range(order_num):
        if order[idx] == 'I':
            x = int(order[idx+1])
            y = int(order[idx+2])

            s = list(map(int,order[idx+3:idx+3+y]))
            code[x:x]=s
            idx += y+3

    print(f"#{tc+1}", *code[:10])


