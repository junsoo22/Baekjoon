import sys
from collections import deque
input=sys.stdin.readline

m,n,k=map(int,input().split())
g=[[0]*n for _ in range(m)]
visited=[[False]*n for _ in range(m)]
for i in range(k):
    lx,ly,rx,ry=map(int,input().split())
    for j in range(ry-ly):
        for k in range(rx-lx):
            g[ly+j][lx+k]=1

dx=[0,0,1,-1]
dy=[1,-1,0,0]
def bfs(x,y):
    area=1
    queue=deque()
    queue.append((x,y))
    visited[x][y]=True
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            wx=dx[i]+x
            wy=dy[i]+y
            if 0<=wx<m and 0<=wy<n and g[wx][wy]==0 and not visited[wx][wy]:
                area+=1
                queue.append((wx,wy))
                visited[wx][wy]=True
    result.append(area)
result=[]
for i in range(m):
    for j in range(n):
        if g[i][j]==0 and not visited[i][j]:
            bfs(i,j)

result.sort()
print(len(result))
print(*result)
