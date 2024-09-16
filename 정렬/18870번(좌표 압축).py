import sys

n=int(input())

arr=list(map(int,sys.stdin.readline().split()))

result=sorted(list(set(arr)))   #set으로 중복 없애고 정렬
print(result)

dic={result[i]:i for i in range(len(result))} 

for i in arr:
    print(dic[i],end=" ")