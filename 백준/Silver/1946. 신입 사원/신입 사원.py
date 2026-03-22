import sys

input=sys.stdin.readline

tc=int(input())

for t in range(tc):
    rank=[]
    n=int(input())
    for i in range(n):
        docu_rank,interview_rank=map(int,input().split())

        rank.append((docu_rank,interview_rank))
    rank.sort()

    count=1
    min_interview=rank[0][1]


    for i in range(1,n):
        if rank[i][1]<min_interview:
            count+=1
            min_interview=rank[i][1]
    print(count)

