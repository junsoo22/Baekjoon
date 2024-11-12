#11726번

n=int(input())
arr=[0]*1001


def dp(n):
    if n==1:
        return 1
    if n==2:
        return 2
    if n==3:
        return 3
    if arr[n]!=0:
        return arr[n]
    arr[n]=(dp(n-1)+dp(n-2))%10007
    return arr[n]


print(dp(n))