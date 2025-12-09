from collections import deque

def solution(n, computers):
    def bfs(node):
        queue=deque([node])
        visited[node]=True
        
        while queue:
            cur=queue.popleft()
            for nxt in range(n):
                if computers[cur][nxt]==1 and not visited[nxt]:
                    visited[nxt]=True
                    queue.append(nxt)
                                 
    visited=[False]*n
    cnt=0
    for i in range(n):
        if not visited[i]:
            bfs(i)
            cnt+=1

    

    return cnt