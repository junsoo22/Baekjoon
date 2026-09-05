def solution(arr):
    num = []
    operator = []

    # arr에서 숫자와 연산자를 분리
    # 예: ["1", "-", "3", "+", "5"]
    # num = [1, 3, 5]
    # operator = ["-", "+"]
    for i in range(len(arr)):
        if i % 2 == 0:
            num.append(int(arr[i]))
        else:
            operator.append(arr[i])

    n = len(num)

    # max_dp[i][j]
    # = i번째 숫자부터 j번째 숫자까지 계산했을 때 만들 수 있는 최댓값
    #
    # min_dp[i][j]
    # = i번째 숫자부터 j번째 숫자까지 계산했을 때 만들 수 있는 최솟값
    max_dp = [[0] * n for _ in range(n)]
    min_dp = [[0] * n for _ in range(n)]

    # 숫자 하나만 있는 구간은
    # 최댓값과 최솟값이 모두 자기 자신
    #
    # 예: num = [1, 3, 5]
    # max_dp[0][0] = 1
    # max_dp[1][1] = 3
    # max_dp[2][2] = 5
    for i in range(n):
        max_dp[i][i] = num[i]
        min_dp[i][i] = num[i]

    # 구간의 길이를 2부터 n까지 증가시키면서 계산
    #
    # 예: num = [1, 3, 5, 8]
    #
    # length = 2
    # 1-3
    # 3+5
    # 5-8
    #
    # length = 3
    # 1-3+5
    # 3+5-8
    #
    # length = 4
    # 1-3+5-8
    for length in range(2, n + 1):

        # 현재 구간의 시작 위치 i
        for i in range(n - length + 1):

            # 현재 구간의 끝 위치 j
            j = i + length - 1

            # 최대값을 구해야 하므로 아주 작은 값으로 초기화
            max_dp[i][j] = float("-inf")

            # 최소값을 구해야 하므로 아주 큰 값으로 초기화
            min_dp[i][j] = float("inf")

            # i ~ j 구간을 k 위치에서 나눠봄
            #
            # 예: 1 - 3 + 5
            #
            # k = 0
            # 1 | - | 3 + 5
            #
            # k = 1
            # 1 - 3 | + | 5
            for k in range(i, j):

                # 현재 두 구간 사이의 연산자가 +
                if operator[k] == "+":

                    # 최댓값을 만들려면
                    # 왼쪽 최대 + 오른쪽 최대
                    max_candidate = (
                        max_dp[i][k]
                        + max_dp[k + 1][j]
                    )

                    # 최솟값을 만들려면
                    # 왼쪽 최소 + 오른쪽 최소
                    min_candidate = (
                        min_dp[i][k]
                        + min_dp[k + 1][j]
                    )

                # 현재 연산자가 -
                else:

                    # A - B의 값을 최대화하려면
                    # A는 크게, B는 작게 만들어야 함
                    #
                    # 최대 = 왼쪽 최대 - 오른쪽 최소
                    max_candidate = (
                        max_dp[i][k]
                        - min_dp[k + 1][j]
                    )

                    # A - B의 값을 최소화하려면
                    # A는 작게, B는 크게 만들어야 함
                    #
                    # 최소 = 왼쪽 최소 - 오른쪽 최대
                    min_candidate = (
                        min_dp[i][k]
                        - max_dp[k + 1][j]
                    )

                # k를 여러 위치에서 잘라보면서
                # 가장 큰 값을 저장
                max_dp[i][j] = max(
                    max_dp[i][j],
                    max_candidate
                )

                # 가장 작은 값을 저장
                min_dp[i][j] = min(
                    min_dp[i][j],
                    min_candidate
                )

    # 0번째 숫자부터 마지막 숫자까지
    # 전체 식에서 만들 수 있는 최댓값 반환
    return max_dp[0][n - 1]