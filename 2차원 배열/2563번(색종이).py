n=int(input())
arr=[[0]*100 for i in range(100)]
result=0

for i in range(n):
    a,b=map(int, input().split())
    for j in range(a,a+10):
        for k in range(b,b+10):
            arr[j][k]=1     #겹치는 부분도 1로 유지되므로 중복 방지
result=0
for i in range(100):
    result+=arr[i].count(1)
print(result)


