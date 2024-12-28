import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6) 
n,m,r=map(int,input().split())

visited=[0 for _ in range(n+1)]
g=[[] for i in range(n+1)]
result=[]
count=1
for i in range(m):
    u,v=map(int,input().split())
    g[v].append(u)
    g[u].append(v)

for i in range(1,n+1):
    g[i].sort()

def dfs(r):
    global count
    visited[r]=count
    for i in g[r]:
        if visited[i]==0:
            count+=1
            dfs(i)

dfs(r)
for i in range(1,n+1):
    print(visited[i])