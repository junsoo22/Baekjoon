def solution(arr1, arr2):
    answer = [[]]
    # 결과 행렬 초기화
    rows_A = len(arr1)
    cols_A = len(arr1[0])
    cols_B = len(arr2[0])
    
    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]
    
    # 3중 for문을 이용한 행렬곱 연산
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += arr1[i][k] * arr2[k][j]
    print(result)
    return result