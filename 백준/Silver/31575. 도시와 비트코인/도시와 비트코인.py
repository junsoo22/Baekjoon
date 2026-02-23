
from collections import deque

def bfs(x,y):
    queue=deque()
    queue.append((x,y))
    visited[x][y]=True

    dx=[1,0]
    dy=[0,1]

    while queue:
        x,y=queue.popleft()
        if x==m-1 and y==n-1:
            print("Yes")
            return
        for i in range(2):
            wx=dx[i]+x
            wy=dy[i]+y

            if 0<=wx<m and 0<=wy<n and city[wx][wy]==1 and visited[wx][wy]==False:
                queue.append((wx,wy))
                visited[wx][wy]=True

    
    print("No")


n,m=map(int,input().split())

city=[]
visited=[[False for _ in range(n)]for _ in range(m)]

for i in range(m):
    city.append(list(map(int,input().split())))



bfs(0, 0)