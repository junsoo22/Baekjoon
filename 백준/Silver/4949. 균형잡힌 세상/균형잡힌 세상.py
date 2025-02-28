from collections import deque



while True:
    stack=[]
    flag=True
    sentence=input()
    if sentence==".":
        break
    for i in sentence:
        if i=="[" or i=="(":
            stack.append(i)
        elif i=="]":
            if len(stack)==0 or stack[-1]!="[":
                flag=False
                break
            stack.pop()
        elif i==")":
            if len(stack)==0 or stack[-1]!="(":
                flag=False
                break
            stack.pop()

    if stack:
        flag=False
    if flag:
        print("yes")
    else:
        print("no")
                

