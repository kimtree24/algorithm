def solution(dirs):
    # dfs
    # 방향
    direction = {"U": (1,0), "D": (-1,0), "R": (0,1), "L": (0,-1)}
    # 방문 경로 집합 (좌표쌍 튜플로)
    visited_edges = set()
    
    # 관리해야 할 것
    # 카운트는 리턴으로 / 다음좌표-> dirs를 돌 idx관리 필요 / 현재좌표
    def dfs(idx, crow, ccol, cnt):
        # 탈출조건 -> dirs 다 탐색한 경우
        if idx == len(dirs):
            return cnt
        # 이번 턴 이동
        nrow, ncol = direction[dirs[idx]][0] + crow, direction[dirs[idx]][1] + ccol
        # 이동 가부 결정
        if not (0 <= nrow <= 10 and 0 <= ncol <= 10):
            return dfs(idx + 1, crow, ccol, cnt)
        
        # 경로 판단
        edge = ((crow, ccol), (nrow, ncol))
        reverse_edge = ((nrow, ncol), (crow, ccol))
        
        # 처음 가보는 경로라면 카운트 증가
        if edge not in visited_edges and reverse_edge not in visited_edges:
            visited_edges.add(edge)
            visited_edges.add(reverse_edge)
            return dfs(idx + 1, nrow, ncol, cnt + 1)
        else:
            # 이미 간 길이면 cnt 변화 없음
            return dfs(idx + 1, nrow, ncol, cnt)
        
    return dfs(0,5,5,0)