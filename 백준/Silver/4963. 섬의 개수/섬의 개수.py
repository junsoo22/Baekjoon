from collections import deque
import sys
input=sys.stdin.readline

dx=[0,0,1,-1,-1,1,1,-1]
dy=[1,-1,0,0,1,1,-1,-1]

def bfs(x,y):
    queue=deque()
    queue.append((x,y))
    visited[x][y]=True
    while queue:
        x,y=queue.popleft()
        for i in range(8):
            wx=x+dx[i]
            wy=y+dy[i]

            if 0<=wx<h and 0<=wy<w and g[wx][wy]==1 and not visited[wx][wy]:
                visited[wx][wy]=True
                queue.append((wx,wy))
    

while True:
    total=0
    w,h=map(int, input().split())
    g=[]
    visited = [[False] * w for _ in range(h)]
    queue=deque()
    for i in range(h):
        mapp=list(map(int,input().split()))
        g.append(mapp)
    for i in range(h):
        for j in range(w):
            if g[i][j]==1 and not visited[i][j]:
                bfs(i,j)
                total+=1

    if w==0 and h==0:
        break

    print(total)