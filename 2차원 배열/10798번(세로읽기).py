arr=[]
max=0
for i in range(5):
    n=list(input())
    arr.append(n)
    if max<len(arr[i]):
        max=len(arr[i])

for j in range(max):
    for k in range(5):
        
        if j>=len(arr[k]):
            continue
        print(arr[k][j],end="")