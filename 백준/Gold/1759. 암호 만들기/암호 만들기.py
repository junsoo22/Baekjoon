from itertools import combinations, permutations

l,c=map(int,input().split())

arr=list(map(str,input().split() ))

arr.sort()

vowels=['a','e','i','o','u']

combi=list(combinations(arr,l))

result=[]
for i in combi:
    a=list(i)

    vCount=0
    cCount=0
    for j in a:
        if j in vowels:
            vCount+=1
        else:
            cCount+=1
    if vCount>=1 and cCount>=2:
        print(''.join(i))
    