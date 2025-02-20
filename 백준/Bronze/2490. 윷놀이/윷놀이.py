
for i in range(3):
    cnt=0
    arr=list(map(int,input().split()))
    for j in arr:
        if j==1:
            cnt+=1
    if cnt==1:
        print("C")
    elif cnt==2:
        print("B")
    elif cnt==3:
        print("A")
    elif cnt==4:
        print("E")
    else:
        print("D")

    
