from collections import deque

def bfs(x,y):
    queue=deque()
    queue.append((x,y))
    visited[x][y]=True
    cells=[(x,y)]
    dx=[-1,0,1,0]
    dy=[0,-1,0,1]

    while queue:

        x,y=queue.popleft()

        for i in range(4):
            wx=x+dx[i]
            wy=y+dy[i]

            if 0<=wx<n and 0<=wy<n and visited[wx][wy]==False and graph[wx][wy]==1:
                queue.append((wx,wy))
                visited[wx][wy]=True
                cells.append((wx,wy))
    # print(cells)
    result.append(len(cells))
    # print(result)
    

n=int(input())

graph=[]
for i in range(n):
    graph.append(list(map(int,input().strip())))
# print(graph)
result=[]
visited=[[False]*n for _ in range(n)]
cnt=0
for i in range(n):
    for j in range(n):
        if graph[i][j]==1 and not visited[i][j]:
            bfs(i,j)
            cnt+=1
print(cnt)
result.sort()
for i in range(len(result)):
    print(result[i])