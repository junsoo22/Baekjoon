from collections import deque

def can_convert(a,b):   #두 단어가 한 글자만 다르면 True
    diff=0
    for i in range(len(a)):
        if a[i]!=b[i]:
            diff+=1
    return diff==1

def solution(begin, target, words):
    answer = 0
    cnt=0
    

    
    queue=deque()
    queue.append((begin,0))
    
    visited=set()
    
    if target not in words:
        return 0
    
    while queue:
        word,cnt=queue.popleft()
        
        if word==target:
            return cnt
        
        for w in words:
            if w not in visited and can_convert(word,w):
                visited.add(w)
                queue.append((w,cnt+1))
                print(queue)
                print(visited)
    
        
    return 0
