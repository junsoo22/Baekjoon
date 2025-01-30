from collections import deque

n=int(input())
g=[]

for i in range(n):
    m=list(map(int,input()))
    g.append(m)

def bfs(x,y):
    count=1
    queue=deque()
    queue.append((x,y))
    visited[x][y]=True
  
    while queue:

        s=len(queue)
        for i in range(s):
            x,y=queue.popleft()
            for i in range(4):
                wx=dx[i]+x
                wy=dy[i]+y

                if 0<=wx<n and 0<=wy<n and not visited[wx][wy] and g[wx][wy]==1:

                    queue.append((wx,wy))
                    visited[wx][wy]=True
                    count+=1
    result.append(count)
        
dx=[0,0,1,-1]
dy=[1,-1,0,0]
count=0
total=0
visited=[[False]*n for i in range(n)]

result=[]
for i in range(n):
    for j in range(n):
        if g[i][j]==1 and not visited[i][j]:
            bfs(i,j)

result.sort()
print(len(result))
for i in result:
    print(i)