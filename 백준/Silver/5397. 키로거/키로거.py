

tc=int(input())


for i in range(tc):
    arr=list(input())
    left_stack=[]
    right_stack=[]

    for i in arr:
        if i=="<":
            if left_stack:
                right_stack.append(left_stack.pop())

        elif i==">":
            if right_stack:
                left_stack.append(right_stack.pop())

        elif i=="-":
            if left_stack:
                left_stack.pop()

        else:
            left_stack.append(i)
    print("".join(left_stack) + "".join(reversed(right_stack)))