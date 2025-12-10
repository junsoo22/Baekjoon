from collections import deque

def solution(maps):
    
    cnt=0
    dx=[-1,0,1,0]
    dy=[0,-1,0,1]
    
    n=len(maps)
    m=len(maps[0])
    
    visited=[[False for _ in range(m)] for _ in range(n)]
    
    queue=deque()
    queue.append((0,0,1))    #x,y,이동거리
    visited[0][0]=True
    
    while queue:
        x,y,dist=queue.popleft()
        
        if x==n-1 and y==m-1:
            return dist
        
        for i in range(4):
            wx=x+dx[i]
            wy=y+dy[i]
            
            if 0<=wx<n and 0<=wy<m:
                if maps[wx][wy]==1 and not visited[wx][wy]:
                    
                    visited[wx][wy]=True
                    queue.append((wx,wy,dist+1))
    
    
    return -1