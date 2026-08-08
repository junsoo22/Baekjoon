from collections import Counter
def solution(k, tangerine):
    answer = 0
    counter = Counter(tangerine)
    sorted_counter=sorted(counter.values(),reverse=True)
    sm = 0
    for i in range(len(sorted_counter)):
        sm += sorted_counter[i]
        if sm >= k:
            answer = i + 1
            break

    return answer