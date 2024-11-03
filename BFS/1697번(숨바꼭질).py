from collections import deque

n,k=map(int,input().split())
visited=[0]*100
graph=[]

def bfs(n):
    queue=deque()
    queue.append(n)
    while queue:
        print("현재 queue ",*queue)
        print()
        print("현재 visited", visited )
        q=queue.popleft()
        print(q) 
        if q==k:
            print(visited[q])
            break
        for nx in (q-1,q+1,q*2):
            if 0<=nx<=100000 and not visited[nx]:
                visited[nx]=visited[q]+1
                print("넣을 값",nx)
                queue.append(nx)
bfs(n)