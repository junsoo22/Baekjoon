n=int(input())
arr=[0]*10001

for i in range(n):
    x=int(input())
    arr[x]+=1


for i in range(10001):
    while arr[i]!=0:
        print(i)
        arr[i]-=1