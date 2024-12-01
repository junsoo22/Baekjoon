import heapq
import sys
input = sys.stdin.readline
INF=int(1e9)

V,E=map(int,input().split())
k=int(input())
graph=[[] for _ in range(V+1)]
dist=[INF]*(V+1)
for i in range(E):
    u,v,w=map(int,input().split())
    graph[u].append((v,w))

q=[]

def dijkstra(k):

    heapq.heappush(q,(0,k))
    dist[k]=0

    while q:
        distance,node=heapq.heappop(q)
        for adj,cost in graph[node]:
            
            result=cost+distance
            if result<dist[adj]:
                dist[adj]=result
                heapq.heappush(q,(result,adj))


dijkstra(k)

for i in range(1,len(dist)):
    if dist[i]==INF:
        print("INF")
    else:
        print(dist[i])