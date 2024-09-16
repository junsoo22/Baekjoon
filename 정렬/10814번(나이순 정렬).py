import sys

n=int(input())
arr=[]
result=[]
for i in range(n):
    arr.append(list(map(str,sys.stdin.readline().split())))

arr.sort(key=lambda x:int(x[0]))

for i in arr:
    print(i[0],i[1])
