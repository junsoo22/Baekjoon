
s=list(input())

result=[]

for i in range(len(s)):
    if s[i]==")":

        result.append(s[i])
        if len(result)>1 and result[-2]=='(':
            result.pop()
            result.pop()
    elif s[i]=='(':
        result.append(s[i])

print(len(result))        