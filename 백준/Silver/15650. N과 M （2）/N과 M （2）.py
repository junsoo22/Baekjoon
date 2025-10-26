
def dfs(start,depth):

    #개수에 맞게 꽉 찼다면 결과 출력
    if depth==m:
        print(' '.join(map(str, selected)))
        return

    #Start부터 n까지 반복
    for i in range(start,n+1):
        selected[depth]=i
        dfs(i+1,depth+1)




n,m=map(int,input().split())

selected=[0]*m

dfs(1,0)
