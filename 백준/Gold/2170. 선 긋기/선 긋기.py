import sys

input=sys.stdin.readline
n=int(input())
queue=[]
for i in range(n):
    x,y=map(int,input().split())
    queue.append((x,y))

queue.sort()
result=0
sx,sy=queue[0]
result=sy-sx
for i in range(1,len(queue)):
    dx,dy=queue[i]
    if dx<=sy<dy:
        result+=(dy-sy)
    elif sx<=dx<=sy and sx<=dy<=sy:
        continue
    elif dx>=sy:
        result+=(dy-dx)
    sx,sy=dx,dy
print(result)


