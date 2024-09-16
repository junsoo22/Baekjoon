import sys

n=int(input())
arr=[]
for i in range(n):
    arr.append(sys.stdin.readline().strip())
tmp=set(arr)         #중복 제거 위해 

result=list(tmp)
result.sort()
result.sort(key=len)

for i in result:
    print(i)





