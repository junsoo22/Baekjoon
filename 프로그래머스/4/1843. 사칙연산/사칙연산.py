def solution(arr):
    answer = -1
    dp = []
    num = []
    operator = []
    # 숫자, 연산자 분리
    for i in range(len(arr)):
        if i%2==0:
            num.append(int(arr[i]))
        else:
            operator.append(arr[i])
    n = len(num)
    max_dp = [[0] * n for _ in range(n)]
    min_dp = [[0] * n for _ in range(n)]

    for i in range(n):
        max_dp[i][i]=num[i]
        min_dp[i][i]=num[i]
    
    # print(min_dp)
    # print(max_dp)
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            max_dp[i][j] = float("-inf")
            min_dp[i][j] = float("inf")
            for k in range(i, j):
                # print("i, j, k =", i, j, k)
                # print("연산자 =", operator[k])
                if operator[k] == "+":
                    max_candidate = max_dp[i][k] + max_dp[k+1][j]
                    min_candidate = min_dp[i][k] + min_dp[k+1][j]

                else:  # "-"
                    max_candidate = max_dp[i][k] - min_dp[k+1][j]
                    min_candidate = min_dp[i][k] - max_dp[k+1][j]
                # print(max_candidate)
                # print(min_candidate)
                max_dp[i][j] = max(max_dp[i][j], max_candidate)
                min_dp[i][j] = min(min_dp[i][j], min_candidate)
    # print(max_dp)
    # print(min_dp)
    return max_dp[0][n-1]