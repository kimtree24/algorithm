from collections import deque

def solution(board):
    # board를 2차원 배열로 변환
    # R 위치 찾기, G 위치 찾기
    # deque에 R 위치 넣기
    # bfs 수행하기
        # D 만날 때 까지 움직이기 -> 이걸 이동 1로 표현
        # 이동 끝났을 때 위치가 G이면 stop
        # 이동 다 끝났는데도 G 못갔으면 -1 return
    len_r = len(board)
    len_c = len(board[0])
    
    # R 위치, G 위치 찾기
    for r in range(len_r):
        for c in range(len_c):
            if board[r][c] == 'R':
                sr, sc = r, c
            if board[r][c] == 'G':
                gr, gc = r, c
    
    dirs = [(1,0), (-1,0), (0, -1), (0, 1)]
    visited = [[False for _ in range(len_c)] for _ in range(len_r)]
    
    q = deque([(sr, sc, 0)])
    visited[sr][sc] = True
    
    while q:
        cr, cc, cnt = q.popleft()
        if (cr, cc) == (gr, gc):
            return cnt
        
        for dr, dc in dirs:
            nr, nc = cr, cc
            while True:
                tr, tc = nr + dr, nc + dc
                if 0 <= tr < len_r and 0 <= tc < len_c and board[tr][tc] != 'D':
                    nr, nc = tr, tc
                else:
                    break
            if not visited[nr][nc]:
                q.append((nr, nc, cnt + 1))
                visited[nr][nc] = True
    return -1