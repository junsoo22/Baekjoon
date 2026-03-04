import sys
input=sys.stdin.readline
s=list(input().rstrip())
t=list(input().rstrip())
 
result=0

# 문자열 뒤에 A 추가->A pop
# 문자열 뒤집고 뒤에 B 추가->B pop하고 문자열 뒤집기

for i in range(len(t)):
    if len(s)==len(t):
        if s==t:
            result=1
            break
    if t[-1]=='A':
        t.pop()
        # print(t)
    elif t[-1]=='B':
        t.pop()
        t.reverse()
        # print(t)
print(result)


