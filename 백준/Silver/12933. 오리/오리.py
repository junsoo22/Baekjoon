
quack="quack"
sound=list(input())
visited=[False for _ in range(len(sound))]
ans=0

if len(sound)%5!=0:
    print(-1)
    exit()
for i in range(len(sound)):
    if sound[i]=='q' and not visited[i]:
        first=True
        idx=0
        for j in range(i,len(sound)):
            if sound[j]==quack[idx] and not visited[j]:
                visited[j]=True
                if sound[j]=='k':
                    if first:
                        ans+=1
                        first=False
                    idx=0
                else:
                    idx+=1
                
if not all(visited) or ans==0:
    print(-1)
else:
    print(ans)
