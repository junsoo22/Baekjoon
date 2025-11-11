def dfs(idx,sm):
    global ans
    
    #가지치기
    if ans<=sm:
        return
    
    if idx==n:
        ans=min(ans,sm)
        return

    for i in range(n):
        if visited[i]==0:
            visited[i]=1
            dfs(idx+1,sm+arr[idx][i])
            visited[i]=0

t=int(input())

for tc in range(t):
    n=int(input())
    arr=[]
    for i in range(n):
        arr.append(list(map(int,input().split())))
    ans=n*10
    visited=[0 for i in range(n)]
    dfs(0,0)
    print(f"#{tc+1} {ans}")

