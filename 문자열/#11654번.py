#11654번
# a=int(input())
# b=input()
# sum=0
# for i in range(len(b)):
#     sum+=int(b[i])
# print(sum)

#10809번
# import string
# s=input()
# lower=[i for i in string.ascii_lowercase]
# for j in lower:
#         if j in s:
#             print(s.find(j))
#         else:
#             print(-1)

#2675번
# t=int(input())

# for i in range(t):
#     arr=[]
#     r,s=input().split()
#     for j in s:
#         arr.append(int(r)*j)
#     print("".join(arr))

#1152번
# x=input()
# count=0
# arr=x.split()
# print(len(arr))

#2908번      #문자열 뒤집기-> 리스트로 바꿔서 reverse 쓰고 다시 join으로 합쳐서 문자열로 만들기
# a,b=input().split()
# a=list(a)
# a.reverse()
# a="".join(a)
# b=list(b)
# b.reverse()
# b="".join(b)
# if int(a)<int(b):
#     print(b)
# else:
#     print(a)

#5622번
# str=input()
# time=0
# for i in str:
#     if i in "ABC":
#         time+=3
#     elif i in "DEF":
#         time+=4
#     elif i in "GHI":
#         time+=5
#     elif i in "JKL":
#         time+=6
#     elif i in "MNO":
#         time+=7
#     elif i in "PQRS":
#         time+=8
#     elif i in "TUV":
#         time+=9
#     elif i in "WXYZ":
#         time+=10
#     else:
#         time+=11
# print(time)


#11718번
# while True:
#     try:
#         a=input()
#     except EOFError:
#         break
