a,b=map(int,input().split())

arr=[[0]*i for i in range(1,a+2)]


arr[0][0]=1
arr[1][0]=1
arr[1][1]=1

for i in range(2,a+1):
    arr[i][0]=1
    for j in range(1,i):
        arr[i][j]=arr[i-1][j-1]+arr[i-1][j]
    arr[i][i]=1

print(arr[a][b]%10007)