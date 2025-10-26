t = int(input())
arr = [1,2,3,4,5,6,7,8,9,10,11,12]

def dfs(idx, selected, n, k):
    global count

    # 가지치기 1: 선택 수가 n개를 넘으면 중단
    if len(selected) > n:
        return
    
    # 가지치기 2: 합이 이미 k보다 크면 중단
    if sum(selected) > k:
        return
    
    # 종료 조건: 끝까지 탐색했을 때
    if idx == len(arr):
        if len(selected) == n and sum(selected) == k:
            count += 1
        return
    
    # 1️ 현재 숫자 arr[idx]를 선택하는 경우
    dfs(idx + 1, selected + [arr[idx]], n, k)
    
    # 2️ 현재 숫자를 선택하지 않는 경우
    dfs(idx + 1, selected, n, k)


for tc in range(1, t + 1):
    n, k = map(int, input().split())
    count = 0
    dfs(0, [], n, k)
    print(f'#{tc} {count}')
