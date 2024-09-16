t=int(input())
arr=[25,10,5,1]

for i in range(t):
    result=[]
    c=int(input())
    for j in range(len(arr)):
        result.append(c//arr[j])
        c=c%arr[j]
       
    print(*result)
