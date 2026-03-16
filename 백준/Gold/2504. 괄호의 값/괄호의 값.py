from collections import deque
import sys

input=sys.stdin.readline

str=input()

queue=deque()
mul=1
result=0
for i in range(len(str)):
    if str[i] == '(':
        queue.append('(')
        mul *= 2

    elif str[i] == '[':
        queue.append('[')
        mul *= 3
            
    elif str[i]==')':
        if not queue or queue[-1]!='(':
            print(0)
            exit()
        if str[i-1]=='(':
            result+=mul

        queue.pop()
        mul//=2

    elif str[i]==']':
        if not queue or queue[-1]!='[':
            print(0)
            exit()
        if str[i-1]=='[':
            result+=mul

        queue.pop()
        mul//=3
if queue:
    print(0)
else:
    print(result)