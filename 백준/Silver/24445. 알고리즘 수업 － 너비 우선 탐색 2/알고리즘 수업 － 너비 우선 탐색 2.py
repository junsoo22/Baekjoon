import sys
from collections import deque
input = sys.stdin.readline

def bfs(r):
    global count
    q=deque([r])

    visited[r]=count

    while q:
        a=q.popleft()
        for j in g[a]:
            if visited[j]==0:
                count+=1
                visited[j]=count
                q.append(j)


n,m,r=map(int,input().split())
g=[[]for i in range(n+1)]
q=[]
visited=[0]*(n+1)


count=1
for i in range(m):
    u,v=map(int,input().split())
    g[u].append(v)
    g[v].append(u)

for j in range(len(g)):
    g[j].sort(reverse=True)

bfs(r)

for i in range(1,len(visited)):
    print(visited[i])