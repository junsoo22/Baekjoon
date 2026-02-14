import math

n,k=map(int,input().split())

room=0
man=[0]*6
woman=[0]*6
for i in range(n):
    s,y=map(int,input().split())
    if s==1:
        man[y-1]+=1
    else:
        woman[y-1]+=1

for i in range(6):
    room+=math.ceil(man[i]/k)
    room+=math.ceil(woman[i]/k)

print(room)