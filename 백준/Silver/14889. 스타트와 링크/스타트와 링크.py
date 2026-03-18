from itertools import combinations, permutations
import sys

input=sys.stdin.readline

n=int(input())
nums=[i for i in range(1,n+1)]
combi = list(combinations(nums, n//2))


skill=[]
s=[]
l=[]
nums=set(nums)

for i in combi:
    i=set(i)
    s.append(i)
    l.append(nums-i)

for i in range(n):
    skill.append(list(map(int,input().split())))

result=9999
sumA=0
sumB=0
answer=0
for i in range(len(s)):

    a=list(s[i])
    b=list(l[i])

    sumA=0
    sumB=0
    for j in a:
        for k in a:
            sumA+=skill[j-1][k-1]


    for j in b:
        for k in b:
            sumB+=skill[j-1][k-1]


    answer=abs(sumA-sumB)
    result=min(answer,result)
print(result)






