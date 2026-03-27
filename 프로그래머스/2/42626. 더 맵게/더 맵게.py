import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    cnt=0
    while len(scoville)>=2:
        min_scov=heapq.heappop(scoville)
        # print(min_scov)
        if min_scov>=K:
            return cnt
        else:
            min2_scov=heapq.heappop(scoville)
            # print("min2",min2_scov)
            tmp=min_scov+min2_scov*2
            # print(tmp)
            heapq.heappush(scoville,tmp)
            cnt+=1
    
    if scoville[0]>K:
        return cnt
    else:
        return -1