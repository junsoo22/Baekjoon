

def dfs(idx,sm,limit):
    global ans
    if idx==n:
        if limit<=l:
            ans=max(ans,sm)
        return


    #햄버거 먹는 경우
    dfs(idx+1,sm+burger[idx][0],limit+burger[idx][1])

    #안먹는 경우
    dfs(idx+1,sm,limit)

t=int(input())

for tc in range(t):
    n,l=map(int,input().split())
    burger=[]
    for i in range(n):
        t,k=map(int,input().split())
        burger.append((t,k))
    ans=0
    dfs(0,0,0)
    print(f"#{tc+1} {ans}")