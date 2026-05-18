


for tc in range(10):
    arr = []
    n = int(input())
    for i in range(n):
        arr.append(list(map(int,input().split())))

    answer=0

    for col in range(n):
        col_values = [row[col] for row in arr]
        flag = False
        for i in col_values:
            if i == 1:
                flag = True
            elif i == 2:
                if flag:
                    answer+=1
                    flag = False

    print(f"#{tc+1} {answer}")


