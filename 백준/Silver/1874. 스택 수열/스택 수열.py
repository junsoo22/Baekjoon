n=int(input())

stack=[]
current=1
result=[]
for i in range(n):
    x=int(input())
    while current<=x:

        stack.append(current)
        result.append("+")
        current+=1

    if stack[-1]==x:
        stack.pop()
        result.append("-")
    else:
        print("NO")
        exit(0)
    
print("\n".join(result))

