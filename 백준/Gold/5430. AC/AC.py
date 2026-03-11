from collections import deque
import sys

input=sys.stdin.readline

t=int(input())

for i in range(t):
    p=input()
    n=int(input())
    arr=input().rstrip()

    queue=deque()
    result=""
    reverse=False
    if n==0:
        queue=[]
    else:
        queue=deque(map(int,arr[1:-1].split(',')))
    for j in range(len(p)):
        if p[j]=='R':
            reverse=not reverse

        elif p[j]=='D':
            if len(queue)==0:
                result="error"
                break
            if reverse:
                queue.pop()
            else:
                queue.popleft()

    if result:

        print(result)
    else:
        if reverse:
            queue.reverse()
        print("[" + ",".join(map(str, queue)) + "]")