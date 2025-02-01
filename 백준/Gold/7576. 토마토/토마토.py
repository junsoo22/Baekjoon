from collections import deque

m,n=map(int,input().split())
g=[]
for i in range(n):
    g.append(list(map(int,input().split())))
dx=[0,0,1,-1]
dy=[1,-1,0,0]
queue=deque()
for i in range(n):
    for j in range(m):
        if g[i][j]==1:
            queue.append((i,j))

while queue:
    x,y=queue.popleft()
    for i in range(4):
        wx=dx[i]+x
        wy=dy[i]+y
        if 0<=wx<n and 0<=wy<m and g[wx][wy]==0:
            g[wx][wy]=g[x][y]+1    #익는 날짜를 기록
            queue.append((wx,wy))


max_day=0
for i in g:
    if 0 in i:
        print(-1)
        exit(0)
    max_day=max(max_day,max(i))
print(max_day-1)