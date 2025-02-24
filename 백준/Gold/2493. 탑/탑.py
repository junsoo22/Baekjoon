n=int(input())
top=list(map(int,input().split()))
stack=[]
result=[]
for i in range(n):
    while stack and stack[-1][0]<top[i]:  #현재 탑보다 작은 탑은 pop
        stack.pop()

    if stack:    #스택이 비어있지 않으면 신호를 받은 탑 존재재
        result.append(stack[-1][1]) 

    else:      #신호 받을 탑이 없음음
        result.append(0)
    stack.append((top[i],i+1))      #(탑 높이, 인덱스) 저장

print(*result)

