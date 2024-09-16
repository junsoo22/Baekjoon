
n,m=map(int,input().split())

arr=[]
arr2=[]
for i in range(n):
    a=list(map(int,input().split()))
    arr.append(a)

for i in range(m):
    b=list(map(int,input().split()))
    arr2.append(b)

for i in range(n):
    for j in range(m):
        print(arr[i][j]+arr2[i][j],end=" ")
    print()

