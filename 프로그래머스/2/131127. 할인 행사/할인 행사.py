from collections import Counter
def solution(want, number, discount):
    answer = 0
    n = len(discount)
    s = 0
    e = 10
    product = dict(zip(want,number))
    cnt = 0
    while e<=n:
        arr= discount[s:e]
        counter=Counter(arr)
        if counter == product:
            cnt += 1
                
        s+=1
        e+=1

    return cnt