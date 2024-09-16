import sys
n,b=map(int,sys.stdin.readline().split())

num="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
result=""
while n!=0:
    result+=num[n%b]
    n//=b

print(num[::-1])

    