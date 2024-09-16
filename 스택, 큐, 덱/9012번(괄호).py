import sys

n=int(sys.stdin.readline())

for i in range(n):
    a=sys.stdin.readline()
    if a[0]=='(':
        print(a[0])
