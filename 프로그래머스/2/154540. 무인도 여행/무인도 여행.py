import sys
sys.setrecursionlimit(10000)  # 상단에 추가

def solution(maps):
    def dfs(x, y):
        nonlocal cnt

        visited[x][y] = 1
        
        dx = [-1, 0, 1, 0]
        dy = [0, -1, 0, 1]
        
        for i in range(4):
            wx = x + dx[i]
            wy = y + dy[i]
    
            if 0<= wx < n and 0<= wy <m and visited[wx][wy]==0 and graph[wx][wy] != 'X':
                cnt += int(graph[wx][wy]) 
                dfs(wx,wy)
        
        
    answer=[]
    n = len(maps)     
    m = len(maps[0])     
    graph=[[0] * m for _ in range(n)]
    visited=[[0] * m for _ in range(n)]
    for x in range(n):
        for y in range(m):
            graph[x][y]=maps[x][y]
    for i in range(n):
        for j in range(m):
            if graph[i][j] != 'X' and visited[i][j] == 0:
                cnt = int(graph[i][j])
                dfs(i,j)
                answer.append(cnt)
    if answer:
        return sorted(answer)
    else:
        answer.append(-1)
        return answer
