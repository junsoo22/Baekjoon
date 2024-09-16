#2750번

n=int(input())
sortArr=[]
for i in range(n):
    sortArr.append(int(input()))

sortArr.sort()
for i in sortArr:
    print(i)