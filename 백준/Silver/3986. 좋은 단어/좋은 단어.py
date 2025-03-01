n=int(input())
count=0
for i in range(n):

    word=input()
    stack=[]

    for j in range(len(word)):
        if stack and stack[-1]==word[j]:
            stack.pop()
        else:
            stack.append(word[j])

    if not stack:
        count+=1
print(count)

        
