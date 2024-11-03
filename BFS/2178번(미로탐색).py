from collections import deque

def bfs(x,y):
    global count
    queue=deque()
    queue.append((x,y))

    visited[x][y]=True

    while queue:
        s=len(queue)
        for i in range(s):
            x,y=queue.popleft()
            if x==n-1 and y==m-1:
                print(count+1)
                return
            for i in range(4):
                wx=dx[i]+x
                wy=dy[i]+y
                if wx<0 or wx >=n or wy<0 or wy>=m:
                    continue
                if graph[wx][wy]==0 or visited[wx][wy]==True:
                    continue
                queue.append((wx,wy))
                visited[wx][wy]=True
        count+=1
            

n,m=map(int,input().split())
graph=[[0]*100 for _ in range(100)]

visited=[[False]*100 for _ in range(100)]

for i in range(n):
    s = input().strip()
    for j in range(m):
        graph[i][j] = int(s[j])
dx=[0,0,1,-1]
dy=[1,-1,0,0]
count=0
bfs(0,0)


