T = int(input())

for tc in range(1, T + 1):

    N, M, K = map(int, input().split())

    time = list(map(int, input().split()))

    time.sort()

    possible = True

    for i in range(N):

        t = time[i]

        # 현재까지 생산된 붕어빵 수
        bread = (t // M) * K

        # 현재까지 온 손님 수
        customer = i + 1

        if bread < customer:
            possible = False
            break

    if possible:
        print(f"#{tc} Possible")
    else:
        print(f"#{tc} Impossible")