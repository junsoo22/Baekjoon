def solution(s):
    cnt = 0
    
    for ch in s:
        if ch == '(':
            cnt += 1
        else:  # ')'
            cnt -= 1
        
        # 닫는 괄호가 먼저 나온 경우
        if cnt < 0:
            return False
    
    # 모든 괄호를 처리한 뒤 '('가 남아 있으면 False
    return cnt == 0
