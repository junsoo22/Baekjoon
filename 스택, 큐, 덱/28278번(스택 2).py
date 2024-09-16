import sys
stack=[]

def check_empty(stack):
    if len(stack)==0:
        return 1
    else:
        return 0
 
n=int(input())
for i in range(n):

    a=sys.stdin.readline().split()
    if a[0]=='1':
        stack.append(a[-1])
    elif a[0]=='2':
        if len(stack)!=0:
            print(stack.pop())
        else:
            print(-1)
    elif a[0]=='3':
        print(len(stack))
    elif a[0]=='4':
        print(check_empty(stack))
    elif a[0]=='5':
        if len(stack)!=0:
            print(stack[-1])
        else:
            print(-1)
