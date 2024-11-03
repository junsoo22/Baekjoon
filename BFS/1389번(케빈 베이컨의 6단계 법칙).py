from collections import deque


def bfs(n):
    queue=deque()
    queue.append(n)
    visited[n]=1
    sum=0

    while queue:
        q=queue.popleft()
        for i in graph[q]:
            if not visited[i]:
                queue.append(i)
                visited[i]=visited[q]+1

    for k in range(len(visited)):
        if k==n:
            continue
        sum+=visited[k]
    return sum

n,m=map(int,input().split())
graph=[[] for _ in range(1+n)]
for i in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

result=[]
for j in range(1,n+1):
    
    visited=[0]*(n+1)
    result.append(bfs(j))

x=min(result)
print(result.index(x)+1)