import sys
from collections import deque
input=sys.stdin.readline

n=int(input())
g=[]
adj=[[] for _ in range(n)]
visited=[False]*n
for i in range(n):
    g.append(list(map(int,input().split())))


for k in range(n):
    for i in range(n):
        for j in range(n):
            if g[i][k]==1 and g[k][j]==1:
                g[i][j]=1

for row in g:
    for col in row:
        print(col,end=" ")
    print()