from collections import deque

def crain(r_len, c_len, storage, ch):
    for r in range(r_len):
        for c in range(c_len):
            if storage[r][c] == ch:
                storage[r][c] = '!'
    return


def ziga(r_len, c_len, storage, ch):
    # 패딩 추가
    pad = [['!' for _ in range(c_len + 2)] for _ in range(r_len + 2)]
    for r in range(r_len):
        for c in range(c_len):
            pad[r+1][c+1] = storage[r][c]

    visited = [[False for _ in range(c_len + 2)] for _ in range(r_len + 2)]
    q = deque([(0, 0)])
    visited[0][0] = True

    dirs = [(1,0), (-1,0), (0,1), (0,-1)]
    
    cur_remove = []

    while q:
        cr, cc = q.popleft()

        for dr, dc in dirs:
            nr, nc = cr + dr, cc + dc
            if 0 <= nr < r_len + 2 and 0 <= nc < c_len + 2 and not visited[nr][nc]:
                # 접근 가능
                if pad[nr][nc] == '!':
                    visited[nr][nc] = True
                    q.append((nr, nc))
                # 요청한 컨테이너면 제거하고 접근 가능하게 변경 -> 계속 확장은 안됨
                elif pad[nr][nc] == ch:
                    visited[nr][nc] = True
                    cur_remove.append((nr, nc))
    
    for r, c in cur_remove:
        pad[r][c] = '!'

    # 패딩에서 storage로 복사
    for r in range(r_len):
        for c in range(c_len):
            storage[r][c] = pad[r+1][c+1]
    return

def count(r_len, c_len, storage):
    cnt = 0
    for r in range(r_len):
        for c in range(c_len):
            if storage[r][c] == '!':
                cnt += 1
    return r_len * c_len - cnt
                
def solution(storage, requests):
    
    # 문자열 리스트로 변형
    for i, line in enumerate(storage):
        line_list = list(line)
        storage[i] = line_list
    
    r_len = len(storage)
    c_len = len(storage[0])
    
    for request in requests:
        ch = request[0]
        if len(request) == 1:
            # 지게차
            ziga(r_len, c_len, storage, ch)
        elif len(request) == 2:
            # 크레인
            crain(r_len, c_len, storage, ch)
    ans = count(r_len, c_len, storage)
    return ans