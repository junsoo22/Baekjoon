from collections import deque

def dfs(x,y,depth):
    global count
    visited[x][y]=True
    if x==0 and y==c-1:
        if depth==k:
            count+=1
            return 
    if depth>=k:
        return
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < r and 0 <= ny < c:
            if not visited[nx][ny] and mapp[nx][ny] == '.':
                visited[nx][ny] = True
                dfs(nx, ny, depth + 1)
                visited[nx][ny] = False 
        
    


r,c,k=map(int,input().split())
mapp=[]
visited=[[False for _ in range(c)] for _ in range(r)]

for i in range(r):
    mapp.append(list(input()))

count=0

dfs(r-1, 0, 1)

print(count)

