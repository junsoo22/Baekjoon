from collections import deque

def solution(land):
    n = len(land)
    m = len(land[0])

    visited = [[False] * m for _ in range(n)]
    oil_by_col = [0] * m

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def bfs(x, y):
        q = deque()
        q.append((x, y))
        visited[x][y] = True

        size = 1
        cols = set()
        cols.add(y)

        while q:
            x, y = q.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < n and 0 <= ny < m:
                    if not visited[nx][ny] and land[nx][ny] == 1:
                        visited[nx][ny] = True
                        q.append((nx, ny))
                        size += 1
                        cols.add(ny)

        return size, cols

    for i in range(n):
        for j in range(m):
            if land[i][j] == 1 and not visited[i][j]:
                size, cols = bfs(i, j)

                for col in cols:
                    oil_by_col[col] += size

    return max(oil_by_col)