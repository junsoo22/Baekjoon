import sys
from collections import deque

input=sys.stdin.readline

dx=[1,2,2,1,-1,-2,-2,-1]
dy=[2,1,-1,-2,-2,-1,1,2]

def bfs(x,y):
    queue=deque()
    queue.append((x,y))
    visited[x][y]=True
    while queue:
        x,y=queue.popleft()
        for i in range(8): 
            wx=x+dx[i]
            wy=y+dy[i]
            if 0<=wx<l and 0<=wy<l and not visited[wx][wy]:
                queue.append((wx,wy))
                visited[wx][wy]=True
                g[wx][wy]=g[x][y]+1
            if wx==ex and wy==ey:
                print(g[ex][ey])
                return
        




tc=int(input())

for i in range(tc):
    l=int(input())
    visited=[[False]*l for i in range(l)]
    g=[[0]*l for i in range(l)]

    sx,sy=map(int,input().split())
    ex,ey=map(int,input().split())
    bfs(sx,sy)
    

    