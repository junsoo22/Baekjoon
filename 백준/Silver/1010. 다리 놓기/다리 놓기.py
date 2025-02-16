import sys
sys.setrecursionlimit(10**6)
t=int(input())


def factorial(n):
    dp=[0]*(n+1)
    dp[0]=1
    for i in range(1,n+1):
        dp[i]=dp[i-1] * i
    return dp[-1]


for i in range(t):
    n,m=map(int,input().split())
    result=factorial(m)//(factorial(m-n)*factorial(n))
    print(result)
    