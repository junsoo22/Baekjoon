
def MenOfPassion(arr,n):
    sum=0
    for i in range(n-1):
        for j in range(i,n):
            sum+=arr[i]+arr[j]

    return sum

n=int(input())
total=0
for i in range(n):
    total+=i
print(int((n*(n-1))/2))
print(total)
print(2)