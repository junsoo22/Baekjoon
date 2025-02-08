from collections import deque
import sys
input=sys.stdin.readline

def bfs(r):
    visited[r]=True

    queue=deque()
    queue.append(r)

    while queue:
        a=queue.popleft()
        for i in g[a]:
            if not visited[i]:
                parent[i]=a
                visited[i]=True
                queue.append(i)

n=int(input())
g=[[] for _ in range(n+1)]

parent=[1 for i in range(n+1)]
visited=[False for _ in range(n+1)]

for i in range(n-1):
    x,y=map(int,input().split())
    g[x].append(y)
    g[y].append(x)

bfs(1)

for i in range(2,n+1):
    print(parent[i])