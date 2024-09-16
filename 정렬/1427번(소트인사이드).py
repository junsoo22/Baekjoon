import sys

n=int(sys.stdin.readline())

arr=list(str(n))

arr.sort()
arr.reverse()
for i in range(len(arr)):
    print(arr[i],end="")