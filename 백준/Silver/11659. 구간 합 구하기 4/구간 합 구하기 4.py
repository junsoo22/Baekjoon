import sys

n,m=map(int,sys.stdin.readline().split())
arr=list(map(int,sys.stdin.readline().split()))
sum=0
prefix=[0]
for i in arr:
    sum=sum+i
    prefix.append(sum)

for i in range(m):
    
    a,b=map(int,sys.stdin.readline().split())

    print(prefix[b]-prefix[a-1])


