a=int(input())
b=int(input())
c=int(input())
product=a*b*c
result=str(product)
arr=[0]*10
for i in result:
    arr[ord(i)-48]+=1
for i in arr:
    print(i)