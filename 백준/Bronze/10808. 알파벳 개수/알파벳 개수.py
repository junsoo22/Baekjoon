n=input()
arr=[0]*26
for i in n:
    arr[ord(i)-96-1]+=1
print(*arr)

