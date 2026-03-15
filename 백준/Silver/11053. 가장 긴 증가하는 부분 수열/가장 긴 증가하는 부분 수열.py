n=int(input())

arr=list(map(int,input().split()))

dp=[1 for _ in range(n)]   #arr[i]를 마지막 원소로 가지는 증가 부분 수열의 최대 길이. 자기 자신 하나만으로 길이 1짜리 증가 부분 수열 만들 수 있음.

# for i in range(n):
#     for j in range(i):
#         if arr[i]>arr[j]:
#             dp[i]=max(dp[i],dp[j]+1)
# print(max(dp))

def binary_search(arr, target):
    left,right=0,len(arr)-1
    while left<=right:
        mid=(left+right)//2
#        print("mid",mid)
        if arr[mid]<target:
            left=mid+1
        else:
            right=mid-1
    return left

lst=[arr[0]]   #현재까지 발견된 LIS를 저장하기 위한 리스트
for i in range(1,len(arr)):
    if arr[i]>lst[-1]:
        lst.append(arr[i])
    else:
        index=binary_search(lst,arr[i])
        lst[index]=arr[i]
print(len(lst))