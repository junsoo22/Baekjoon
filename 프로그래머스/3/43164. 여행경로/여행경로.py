from collections import defaultdict

def solution(tickets):
    graph = defaultdict(list)
    
    # 그래프 생성
    for a, b in tickets:
        graph[a].append(b)
    
    # 사전순 정렬
    for key in graph:
        graph[key].sort()
    
    path = ["ICN"]
    n = len(tickets)
    
    def dfs(cur):
        # 모든 항공권 사용 완료
        if len(path) == n + 1:
            return True
        
        for i in range(len(graph[cur])):
            nxt = graph[cur][i]
            
            # 항공권 사용
            graph[cur].pop(i)
            path.append(nxt)
            
            if dfs(nxt):
                return True
            
            # 되돌리기 (백트래킹)
            path.pop()
            graph[cur].insert(i, nxt)
        
        return False
    
    dfs("ICN")
    return path
