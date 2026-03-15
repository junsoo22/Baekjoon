from collections import deque

wheel=[[]]
for i in range(4):  
    wheel.append(deque(map(int,input().strip())))    #1이면 S극, 0이면 N극

k=int(input())

for i in range(k):
    num,direction=map(int,input().split())   #1: 시계방향, 0: 반시계방향
    rotate=[0]*5
    rotate[num]=direction

    for i in range(num,1,-1):
        if wheel[i][6]!=wheel[i-1][2]:
            rotate[i-1]= -rotate[i]
        else:
            break
    
    for i in range(num,4):
        if wheel[i][2]!=wheel[i+1][6]:
            rotate[i+1]=-rotate[i]
        else:
            break

    for i in range(1,5):
        if rotate[i]!=0:
            wheel[i].rotate(rotate[i])

score=0
for i in range(1,5):
    if wheel[i][0]==1:
        score+=2**(i-1)
print(score)