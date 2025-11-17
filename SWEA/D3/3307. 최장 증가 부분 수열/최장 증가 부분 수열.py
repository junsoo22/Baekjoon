
t=int(input())

for tc in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    ans=[0 for _ in range(n)]
    for i in range(n):
        ans[i]=1
        for j in range(i):
            if arr[j]<arr[i]:
                ans[i]=max(ans[i],ans[j]+1)


    print(f"#{tc+1} {max(ans)}")