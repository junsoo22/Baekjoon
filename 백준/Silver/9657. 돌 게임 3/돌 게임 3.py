
n=int(input())

arr=[0]*1001

def dp(n):
    arr[1]="SK"
    arr[2]="CY"
    arr[3]="SK"
    arr[4]="SK"
    if n==1:
        return arr[1]
    if n==2:
        return arr[2]
    if n==3:
        return arr[3]
    if n==4:
        return arr[4]
    for i in range(5,n+1):
        if arr[i-1]=="SK" and arr[i-3]=="SK" and arr[i-4]=="SK":
            arr[i]="CY"
        else:
            arr[i]="SK"
        
    return arr[n]

print(dp(n))
