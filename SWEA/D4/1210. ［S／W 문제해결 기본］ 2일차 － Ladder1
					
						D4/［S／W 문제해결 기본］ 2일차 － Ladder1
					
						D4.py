for tc in range(10):

    T = int(input())

    arr = [list(map(int, input().split())) for _ in range(100)]

    # 도착지점(2) 찾기
    x, y = 99, 0

    for j in range(100):
        if arr[99][j] == 2:
            y = j
            break

    # 아래 -> 위로 역추적
    while x > 0:

        # 왼쪽 길이 있으면
        if y > 0 and arr[x][y - 1] == 1:

            while y > 0 and arr[x][y - 1] == 1:
                arr[x][y] = 0
                y -= 1

        # 오른쪽 길이 있으면
        elif y < 99 and arr[x][y + 1] == 1:

            while y < 99 and arr[x][y + 1] == 1:
                arr[x][y] = 0
                y += 1

        # 위로 이동
        x -= 1

    print(f"#{T} {y}")