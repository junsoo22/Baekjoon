
t=int(input())

for tc in range(t):
    n,k=map(int,input().split())
    arr=[]
    for i in range(n):
        arr.append(list(map(int,input().split())))

    ans=0
    #가로 확인
    for i in range(n):
        cnt=0
        for j in range(n):
            if arr[i][j]==1:
                cnt+=1
            else:
                if cnt==k:
                    ans+=1
                cnt=0
        if cnt==k:
            ans+=1

    #세로 확인
    for j in range(n):
        cnt=0
        for i in range(n):
            if arr[i][j]==1:
                cnt+=1
            else:
                if cnt==k:
                    ans+=1
                cnt=0
        if cnt==k:
            ans+=1
    print(f"#{tc+1} {ans}")