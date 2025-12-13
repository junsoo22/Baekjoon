def solution(brown, yellow):
    total = brown + yellow
    print(int(total**0.5))
    # h는 3 이상이어야 함(테두리 때문에)
    for h in range(3, int(total**0.5) + 1):
        if total % h != 0:
            continue
        
        w = total // h
        print(w)
        
        # 노란색 넓이 조건 확인
        if (w - 2) * (h - 2) == yellow:
            return [w, h]
