
def is_increase(num):
    s=str(num)
    for i in range(1,len(s)):
        if s[i]<s[i-1]:
            return False

    return True

t=int(input())

for tc in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    result=[]
    max_val=-1
    for i in range(n):
        for j in range(i):
            prod=arr[i]*arr[j]
            if is_increase(prod):
                max_val=max(max_val,prod)
    print(f"#{tc+1} {max_val}")



