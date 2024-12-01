import sys
input = sys.stdin.readline

n,m=map(int,input().split())
arr=[]
for i in range(n):
    a=list(map(int,input().split()))
    arr.append(a)

sum=0

prefix = [[0]*(n+1) for i in range(n+1)]

for j in range(1,n+1):
    for k in range(1,n+1):
        prefix[j][k]=prefix[j][k-1]+prefix[j-1][k]-prefix[j-1][k-1]+arr[j-1][k-1]

for k in range(m):
    x1,y1,x2,y2=map(int,input().split())
    print(prefix[x2][y2]-prefix[x2][y1-1]-prefix[x1-1][y2]+prefix[x1-1][y1-1])