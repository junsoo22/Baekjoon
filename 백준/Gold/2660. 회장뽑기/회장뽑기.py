from collections import deque

def bfs(node):
    visited=[False for _ in range(n+1)]
    queue=deque()
    queue.append(node)

    visited[node]=True

    while queue:
        cur=queue.popleft()

        for next in graph[cur]:

            if not visited[next]:

                queue.append(next)
                visited[next]=True
                result[node][next]=result[node][cur]+1




n=int(input())

graph=[[] for _ in range(n+1)]

result=[[0 for _ in range(n+1)] for _ in range(n+1)]

while True:
    a,b=map(int,input().split())
    if a==-1 and b==-1:
        break
    graph[a].append(b)
    graph[b].append(a)


for i in range(1,n+1):
    bfs(i)


answer=[]
for i in range(1,n+1):
    length=max(result[i])
    answer.append(length)

score=min(answer)
num=answer.count(score)


print(score, num)
candidate=[]
for i in range(len(answer)):
    if answer[i]==score:
        candidate.append(i+1)
print(*candidate)

