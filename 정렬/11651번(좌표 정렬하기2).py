import sys

n=int(input())
arr=[]
for i in range(n):
    a=list(map(int,sys.stdin.readline().split()))
    arr.append(a)

arr.sort(key=lambda x:(x[1],x[0]))

for i in arr:
    print(i[0],i[1])