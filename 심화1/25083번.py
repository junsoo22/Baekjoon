#심화

#25083번
#         ,r'"7
#r`-_   ,'  ,/
# \. ". L_r'
#   `~\/
#      |
#      |
# print("         ,r'\"7")
# print("r`-_   ,'  ,/")
# print(" \. \". L_r\'")
# print("   `~\/")
# print("      |")
# print("      |")

#3003번
#킹 1개, 퀸 1개, 룩 2개, 비숍 2개, 나이트 2개, 폰 8개
# a=list(map(int,input().split()))

# b=[1,1,2,2,2,8]
# c=[]
# for i in range(6):
#     c.append(b[i]-a[i])
# print(*c)

#2444번 별 찍기

# n=int(input())   #5
 
# for i in range(n):    # 0 1 2 3 4
#     print(" "*(n-i-1)+"*"*(i*2+1))
# for j in range(n-1,0,-1):
#         print(" "*(n-j)+"*"*(j*2-1))

#1157번
# str=input().upper()

# arr=list(set(str))

# result=[]
# for i in arr:
#     result.append(str.count(i))


# if result.count(max(result))>=2:
#     print("?")
# else:
#     print(arr[result.index(max(result))])

#2941번
#replace이용


# str=input()

# arr=['c=','c-','dz=','d-','lj','nj','s=','z=']
# for i in arr:
#     str=str.replace(i,"0")
# print(len(str))


#1316번
#그룹 단어 체커
# n=int(input())
# count=n
# for i in range(n):
#     str=input()
#     for j in range(len(str)-1):
#         if str[j]==str[j+1]:
#             pass
#         elif str[j] in str[j+1:]:
#             count-=1
#             print(count)
#             break
# print(count)
        
#25206번
gpa=0
total=0
grade={'A+':4.5, "A0":4.0, "B+":3.5,"B0":3.0,"C+":2.5,"C0":2.0,"D+":1.5,"D0":1.0,"F":0.0}
for i in range(20):
    subject, point, rank=map(str,input().split())
    if rank=='P':
        continue
    if rank=="A+":
        gpa+=float(point)*grade['A+']
        total+=float(point)
    elif rank=="A0":
        gpa+=float(point)*grade['A0']
        total+=float(point)
    elif rank=="B+":
        gpa+=float(point)*grade['B+']
        total+=float(point)
    elif rank=="B0":
        gpa+=float(point)*grade['B0']
        total+=float(point)
    elif rank=="C+":
        gpa+=float(point)*grade['C+']
        total+=float(point)
    elif rank=="C0":
        gpa+=float(point)*grade['C0']
        total+=float(point)
    elif rank=="D+":
        gpa+=float(point)*grade['D+']
        total+=float(point)
    elif rank=="D0":
        gpa+=float(point)*grade['D0']
        total+=float(point)
    elif rank=="F":
        gpa+=float(point)*grade['F']
        total+=float(point)

print("{:.6f}".format(gpa/total))