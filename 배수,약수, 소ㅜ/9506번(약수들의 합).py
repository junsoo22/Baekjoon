

while(True):
    arr=[]
    result=0
    flag=False

    n=int(input())
    if n==-1:
        break
    else:
        for i in range(1,n):
            if n%i==0:
                arr.append(i)
        for j in arr:
            result+=j
        if result==n:
            flag=True
        else:
            flag=False
        if flag:
            print(result,"=",end=" ")
            for k in range(len(arr)):
                if k==len(arr)-1:
                    print(arr[k])
                    break
                
                print(arr[k],end=" + ")
        else:
            print(n,"is NOT perfect.")
        


