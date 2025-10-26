def dfs(depth, start):
    global ans

    #종료조건
    if depth==m:
        print(*result)
        return
    

    for i in range(start,n+1):
        result[depth]=i
        dfs(depth+1, i)


n,m=map(int,input().split())
result=[0]*m

dfs(0,1)

