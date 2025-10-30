
def binary_search(arr,target):
    l=1
    r=p
    cnt=0
    while l<=r:
        c=(l+r)//2
        if arr[c]==target:
            return cnt
        elif arr[c]<target:
            l=c
            cnt+=1
        else:
            r=c
            cnt+=1


tc=int(input())
for t in range(tc):
    p,a,b=map(int,input().split())
    arr=[i for i in range(p+1)]

    ansA=binary_search(arr,a)
    ansB=binary_search(arr,b)
    if ansA==ansB:
        print(f"#{t+1} 0")
    elif ansA<ansB:
        print(f"#{t+1} A")
    else:
        print(f"#{t+1} B")
