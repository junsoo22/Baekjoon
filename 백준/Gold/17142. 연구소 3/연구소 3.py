from collections import deque
from itertools import permutations, combinations

def bfs(selected):
    dist=[[-1] *N for _ in range(N)]
    queue=deque()
    for x,y in selected:
        queue.append((x,y))
        dist[x][y]=0
    dx=[0,0,-1,1]
    dy=[1,-1,0,0]

    while queue:
        x,y=queue.popleft()
        for i in range(4):
            wx=dx[i]+x
            wy=dy[i]+y
            if 0<=wx<N and 0<=wy<N:
                if board[wx][wy]!=1 and dist[wx][wy]==-1:
                    queue.append((wx,wy))
                    dist[wx][wy]=dist[x][y]+1
    max_time = 0
    for i in range(N):
        for j in range(N):
            # 빈칸인데 도달 못한 경우
            if board[i][j] == 0:
                if dist[i][j] == -1:
                    return float('inf')
                max_time = max(max_time, dist[i][j])
                
    return max_time


N,M=map(int,input().split())    

board=[]
for _ in range(N):
    board.append(list(map(int,input().split())))
virus=[]
for i in range(N):
    for j in range(N):
        if board[i][j]==2:
            virus.append((i,j))

answer=float('inf')

for comb in combinations(virus,M):
    time=bfs(comb)
    answer=min(answer,time)
if answer==float('inf'):
    print(-1)
else:
    print(answer)