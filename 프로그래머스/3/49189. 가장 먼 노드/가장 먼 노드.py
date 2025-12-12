from collections import deque

def solution(n, edge):
    graph = [[] for _ in range(n + 1)]
    visited = [-1] * (n + 1)   # 거리 저장 (-1 = 미방문)

    # 그래프 생성
    for x, y in edge:
        graph[x].append(y)
        graph[y].append(x)

    # BFS
    queue = deque([1])
    visited[1] = 0   # 시작 노드 거리 0

    while queue:
        cur = queue.popleft()
        for nxt in graph[cur]:
            if visited[nxt] == -1:
                visited[nxt] = visited[cur] + 1
                queue.append(nxt)
    print(visited)
    max_dist = max(visited)
    return visited.count(max_dist)
