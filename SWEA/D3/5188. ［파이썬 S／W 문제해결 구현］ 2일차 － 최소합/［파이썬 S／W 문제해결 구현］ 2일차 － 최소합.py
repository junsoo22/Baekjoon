
def dfs(x,y,sm):
    global ans
    #종료조건
    if x==n-1 and y==n-1:
        ans=min(ans,sm)
        return
    
    #오른쪽으로 가는 경우
    if y+1<n:
        dfs(x,y+1,sm+arr[x][y+1])

    #아래로 가는 경우
    if x+1<n:
        dfs(x+1,y,sm+arr[x+1][y])



tc=int(input())

for t in range(tc):
    n=int(input())
    arr=[]
    for i in range(n):
        arr.append(list(map(int,input().split())))
    ans=10000
    dfs(0,0,arr[0][0])

    print(f"#{t+1} {ans}")
