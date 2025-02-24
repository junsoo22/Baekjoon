#10828번
from sys import stdin
n=int(input())
arr=[]
def pop():
    if len(arr)==0:
        print(-1)
        return
    print(arr[-1])
    arr.pop()
def empty():
    if len(arr)==0:
        print(1)
    else:
        print(0)
def top():
    if len(arr)==0:
        print(-1)
    else:
        print(arr[-1])

for i in range(n):
    string=stdin.readline().rstrip()

    if string[:4]=="push":
        arr.append(int(string[5:]))
    elif string =="pop":
        pop()
    elif string=="size":
        print(len(arr))
    elif string=="empty":
        empty()
    elif string=="top":
        top()
