from collections import Counter
def solution(want, number, discount):
    answer = 0
    dict_zip=dict(zip(want,number))
    # print(dict_zip)
    for i in range(len(discount)-9):
        counter=Counter(discount[i:i+10])
        # print(counter)
        if dict_zip == counter:
            answer += 1
    return answer