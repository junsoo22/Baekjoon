def solution(n, wires):
    answer = n

    # 그래프 만들기
    graph = [[] for _ in range(n + 1)]

    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)

    # 연결된 송전탑 개수 세기
    def dfs(x):
        visited[x] = True
        cnt = 1

        for next_node in graph[x]:
            if not visited[next_node]:
                cnt += dfs(next_node)

        return cnt
    print(graph)
    # 전선 하나씩 끊어보기
    for a, b in wires:

        # 전선 끊기
        graph[a].remove(b)
        graph[b].remove(a)

        visited = [False] * (n + 1)

        # 한쪽 송전탑 개수
        cnt = dfs(1)
        print("cnt",cnt)

        # 두 전력망 개수 차이
        diff = abs(cnt - (n - cnt))
        print("diff",diff)

        answer = min(answer, diff)

        # 전선 다시 연결
        graph[a].append(b)
        graph[b].append(a)

    return answer