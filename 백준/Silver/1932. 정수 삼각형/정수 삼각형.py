n=int(input())
arr=[]
for i in range(n):
    arr.append(list(map(int,input().split())))

dp=[]
for i in range(1,n+1):
    dp.append([0]*i)

dp[0]=arr[0]

for i in range(1,n):
    for j in range(i+1):
        if j==0:
            dp[i][j]=dp[i-1][j]+arr[i][0]

        elif j==i:
            dp[i][i]=dp[i-1][i-1]+arr[i][-1]

        else:
            dp[i][j]=max(dp[i-1][j-1]+arr[i][j],dp[i-1][j]+arr[i][j])
       
print(max(dp[-1]))