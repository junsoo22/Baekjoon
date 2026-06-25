def solution(numbers, target):
    answer = 0

    def dfs(idx, sm):
        nonlocal answer

        if idx == len(numbers):
            if sm == target:
                answer += 1
            return

        dfs(idx + 1, sm + numbers[idx])
        dfs(idx + 1, sm - numbers[idx])

    dfs(0, 0)
    return answer