from collections import deque
import sys
input=sys.stdin.readline

n=list(input().strip())   #커서 왼쪽 스택택
m=int(input())

pointer=len(n)

s=[]     #커서 오른쪽 스택
for i in range(m):

    ip=input().split()
    if ip[0]=="L":
        if n:
            s.append(n.pop())

    elif ip[0]=="D":
        if s:
            n.append(s.pop())
    elif ip[0]=="B":
        if n:
            n.pop()
    else:
        n.append(ip[1])

print("".join(n) + "".join(reversed(s)))