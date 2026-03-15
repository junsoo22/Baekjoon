from collections import deque

def solution(priorities, location):
    q = deque([(p, i) for i, p in enumerate(priorities)])
    print(q)
    order=0
    while q:
        p, i = q.popleft()
        print(p,i)
        # 뒤에 더 높은 우선순위가 있으면 다시 큐 뒤로
        if any(p2 > p for p2, _ in q):
            q.append((p, i))
        else:
            # 출력(실행)
            order += 1
            if i == location:
                return order