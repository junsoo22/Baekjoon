
for tc in range(10):
    N, str = input().split()
    str = list(str)

    idx = 0
    while idx < len(str) -1 :
        if str[idx] == str[idx+1]:

            str = str[:idx] + str[idx+2:]
            idx -= 1


            continue
        idx += 1
    result = "".join(str)
    print(f"#{tc+1}",result)