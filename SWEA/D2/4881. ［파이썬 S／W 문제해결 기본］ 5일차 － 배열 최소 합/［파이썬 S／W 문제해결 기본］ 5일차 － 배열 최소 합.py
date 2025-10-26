
def dfs(idx,sm):   #n 행번호, j: 열번호
    global ans
    if ans<=sm:
        return

    
    #종료조건
    if idx==n:
        ans=min(ans,sm)
        return
    for j in range(len(arr)):
        if visited[j]==0:
            visited[j]=1
            dfs(idx+1, sm+arr[idx][j])
            visited[j]=0

tc=int(input())
for t in range(tc):
    n=int(input())
    arr=[]
    for i in range(n):
        arr.append(list(map(int,input().split())))
    ans=n*10
    visited=[0]*n
    dfs(0,0)
        
    print(f"#{t+1} {ans}")