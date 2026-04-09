from collections import deque

N=int(input())

K=int(input())

board=[[0]*(N) for _ in range(N)]
for i in range(K):
    a,b=map(int,input().split())
    board[a-1][b-1]=1
# print(board)
L=int(input())
turn={}
for i in range(L):
    X,C=input().split()
    turn[int(X)]=C
snake=deque()
# 오른쪽, 아래, 왼쪽, 위
dx=[0,1,0,-1]
dy=[1,0,-1,0]
dir=0
snake.append((0,0))
board[0][0]=2
time=0
while True:
    x,y=snake[-1]
    # print("X,y",x,y)
    time+=1
    wx=dx[dir]+x
    wy=dy[dir]+y

    # 벽 충돌
    if not (0<=wx<N and 0<=wy<N):
        break

    # 자기 몸 충돌
    if board[wx][wy]==2:
        break

      # 사과 먹으면
    if board[wx][wy]==1:
        snake.append((wx,wy))
        board[wx][wy]=2

  
    else:
        snake.append((wx,wy))
        board[wx][wy]=2
        tail_x,tail_y=snake.popleft()
        board[tail_x][tail_y]=0

    # 방향 전환
    if time in turn:
        if turn[time]=='L':
            dir=(dir-1)%4
            # print("dir",dir)
        else:
            dir=(dir+1)%4
            # print("dir2",dir)
        # print("time",time)
print(time)