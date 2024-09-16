n=int(input())
arr=[]
for i in range(1,n):
    if i+sum(map(int,str(i)))==n:
        arr.append(i)
        break
if len(arr)==0:
    print(0)
else:
    print(arr[0])