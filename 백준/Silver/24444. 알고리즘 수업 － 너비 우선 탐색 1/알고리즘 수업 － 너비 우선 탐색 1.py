import sys
from collections import deque

input = sys.stdin.readline

def bfs(r):
    global count
    q = deque([r])  # 큐 초기화
    visited[r] = count

    while q:
        a = q.popleft()  # 큐의 맨 앞에서 꺼냄
        for j in g[a]:
            if visited[j] == 0:
                count += 1
                visited[j] = count
                q.append(j)

# 입력 처리
n, m, r = map(int, input().split())
g = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
count = 1

# 간선 정보 입력
for _ in range(m):
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)

# 인접 리스트 정렬
for j in range(1, n + 1):
    g[j].sort()

# BFS 수행
bfs(r)

# 결과 출력
for i in range(1, n + 1):
    print(visited[i])
