n,m=map(int,(input().split()))
result=[]
board=[]
for _ in range(n):
    board.append(input())

for i in range(n-7):
    for j in range(m-7):
        w=0
        b=0
        for a in range(i,i+8):
            for b in range(j,j+8):
                if(a+b)%2==0:
                    if board[a][b] !='W':
                        w+=1
                    else:
                        b+=1
                else:
                    if board[a][b] !='W':
                        b+=1
                    else:
                        w+=1

        result.append(b)
        result.append(w)

print(min(result))
                
