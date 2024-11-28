from collections import deque

q=[]

n,m=map(int,input().split())
graph=[[]for i in range(n+1)]
degree=[0 for i in range(n+1)]

for i in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    degree[b] += 1
p=deque([])
for i in range(1,n+1):
    if degree[i]==0:
        p.append(i)

while p:
    x=p.popleft()
    print(x,end=" ")
    for i in graph[x]:
        degree[i]-=1
        if degree[i]==0:
            p.append(i)

