from collections import deque

n,m=map(int,input().split())
target=list(map(int,input().split()))
queue=deque()

for i in range(n):
    queue.append(i+1)

count=0
for i in target:
    idx=queue.index(i)     #타켓 숫자의 현재 위치

    #왼쪽 회전이 유리한 경우
    if idx<=len(queue)//2:
        queue.rotate(-idx)
        count+=idx

    else:
        queue.rotate(len(queue)-idx)
        count+=len(queue)-idx

    queue.popleft()

print(count)