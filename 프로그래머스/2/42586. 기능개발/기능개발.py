def solution(progresses, speeds):
    answer = []
    days=[]
    for i in range(len(speeds)):
        remain=100-progresses[i]

        if remain%speeds[i]!=0:
            day=remain//speeds[i]+1
        else:
            day=remain//speeds[i]
        days.append(day)

    cur = days[0]
    cnt = 1
    
    for d in days[1:]:
        print(d)
        if d <=cur:
            cnt+=1
        else:
            answer.append(cnt)
            cur=d
            cnt=1
            
    answer.append(cnt)
        
        
    return answer