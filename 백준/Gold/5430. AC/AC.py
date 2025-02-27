from collections import deque
import sys

input=sys.stdin.readline

t=int(input())
for i in range(t):
    queue=deque()
    p=input()
    n=int(input())
    arr=input().strip()
    if n==0:
        queue=[]
    else:
        queue=deque(map(int,arr[1:-1].split(',')))
    flag=0
    reverse=0
    for i in p:
        if i=="R":
            reverse=not reverse

        elif i=="D":
            if len(queue)==0:
                print("error")
                flag=1
                break
            else:
                if reverse:
                    queue.pop()
                else:
                    queue.popleft() 
    if not flag:
        if reverse:
            queue.reverse()
        print("[" + ",".join(map(str, queue)) + "]")
