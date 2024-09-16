from itertools import combinations


n,m=map(int,input().split())

arr=list(map(int,input().split()))

arr=list(combinations(arr,3))
result=0
max=0
arr2=[]
for i in range(len(arr)):
    sum=0
    for j in range(len(arr[i])):
        sum+=arr[i][j]
    if sum<=m:

        arr2.append(sum)

arr2.sort()
print(arr2[-1])

        
