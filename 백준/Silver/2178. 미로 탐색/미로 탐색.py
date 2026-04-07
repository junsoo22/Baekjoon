from collections import deque

def bfs(x,y):
    global cnt
    queue=deque()
    queue.append((x,y))

    dx=[-1,0,1,0]
    dy=[0,-1,0,1]

    while queue:
        x,y=queue.popleft()
        for i in range(4):
            wx=x+dx[i]
            wy=y+dy[i]
            if 0<=wx<n and 0<=wy<m and maze[wx][wy]==1:
                queue.append((wx,wy))
                maze[wx][wy]=maze[x][y]+1
    return maze[n-1][m-1]


n,m=map(int,input().split())
maze=[]
for i in range(n):
    maze.append(list(map(int,input().strip())))
print(bfs(0,0))