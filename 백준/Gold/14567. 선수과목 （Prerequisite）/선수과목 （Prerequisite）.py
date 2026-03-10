from collections import deque
import sys

input=sys.stdin.readline


n,m=map(int,input().split())

indegree=[0 for _ in range(n+1)]
result=[1 for _ in range(n+1)]
subject=[[] for _ in range(n+1)]

for i in range(m):
    a,b=map(int,input().split())
    subject[a].append(b)
    indegree[b]+=1


queue=deque()
for i in range(1,n+1):  
    if indegree[i]==0:
        queue.append(i)

while queue:
    cur=queue.popleft()

    for next in subject[cur]:
        indegree[next]-=1
        result[next]=max(result[next],result[cur]+1)
        if indegree[next]==0:
            queue.append(next)

for i in range(1,n+1):
    print(result[i], end= ' ')