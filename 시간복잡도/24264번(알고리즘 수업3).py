def MenOfPassion(arr,n):
    sum=0
    for i in range(n):
        for j in range(n):
            sum+=arr[i]+arr[j]
    return sum

n=int(input())
print(n*n)
print(2)