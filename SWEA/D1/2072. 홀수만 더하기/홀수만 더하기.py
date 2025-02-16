n=int(input())

for i in range(n):
    sum=0
    arr=list(map(int,input().split()))
    for j in arr:
        if j%2==0:
            continue
        sum+=j
    print(f'#{i + 1} {sum}')