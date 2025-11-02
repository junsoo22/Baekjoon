from collections import deque

def bfs(start, end):
    queue=deque()
    queue.append(start)
    visited[start]=1

    while queue:
        cur=queue.popleft()
        for next in arr[cur]:
            if visited[next]==0:
                visited[next]=visited[cur]+1 # 거리 갱신
                queue.append(next)

                if next==end:
                    return visited[next]-1

    return 0

t=int(input())

for tc in range(t):
    v,e=map(int,input().split())
    arr=[[] for _ in range(v+1)]
    for i in range(e):
        nodeS,nodeE=map(int,input().split())
        arr[nodeS].append(nodeE)
        arr[nodeE].append(nodeS)
    visited=[0]*(v+1)
    s,g=map(int,input().split())
    ans=bfs(s,g)
    print(f"#{tc+1} {ans}")



