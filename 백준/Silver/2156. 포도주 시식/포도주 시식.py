n=int(input())
wine=[]
dp=[0]*n

for i in range(n):
    amount=int(input())
    wine.append(amount)

if n>0:
    dp[0]=wine[0]
if n>1:
    dp[1]=wine[1]+wine[0]
if n > 2:  # n=2일 때는 dp[2] 계산하지 않음
    dp[2] = max(dp[1], wine[0] + wine[2], wine[1] + wine[2]) 
for i in range(3,n):
    dp[i]=max(dp[i-1],dp[i-2]+wine[i],dp[i-3]+wine[i-1]+wine[i])
print(dp[-1])