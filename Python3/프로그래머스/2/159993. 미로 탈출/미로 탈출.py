from collections import deque
def solution(maps):
    # 좌표 생성
    new_maps = [list(row) for row in maps]
    # 이동 가능 방향 생성 (상, 하, 좌, 우)
    dirs = [(-1,0), (1,0), (0,-1),(0,1)]
    # map크기
    len_row = len(maps)
    len_col = len(maps[0])
    # 시작 지점 찾기
    s = []
    for i,row in enumerate(new_maps):
        for j, col in enumerate(row):
            if col == 'S':
                s.append(i)
                s.append(j)
                break
    # BFS로 s에서 l까지 이동 최단거리 구하기
    to_l_q = deque([s])
    visit_to_l = [[False for _ in range(len_col)] for _ in range(len_row)]
    visit_to_l[s[0]][s[1]] = True
    l = []
    cnt_l = [[0 for _ in range(len_col)] for _ in range(len_row)]
    flag_l = False
    cnt_to_l = 0
    while to_l_q:
        if flag_l:
            break
        r,c = to_l_q.popleft()
        # 다음 이동 방향 특정
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            # 이동가부 판단
            if 0 <= nr < len_row and 0 <= nc < len_col and new_maps[nr][nc] != "X" and not visit_to_l[nr][nc]:
                # 이동
                cnt_l[nr][nc] = cnt_l[r][c] + 1
                # 이동한게 "L"이면 그만 이동
                if new_maps[nr][nc] == "L":
                    l.append(nr)
                    l.append(nc)
                    flag_l = True
                    cnt_to_l = cnt_l[nr][nc]
                    break
                to_l_q.append([nr,nc])
                visit_to_l[nr][nc] = True
    # 이동 불가
    if not l:
        return -1
    # BFS로 l에서 e까지 이동 최단거리 구하기
    to_e_q = deque([l])
    visit_to_e = [[False for _ in range(len_col)] for _ in range(len_row)]
    visit_to_e[l[0]][l[1]] = True
    cnt_e = [[0 for _ in range(len_col)] for _ in range(len_row)]
    flag_e = False
    e = []
    cnt_to_e = 0
    while to_e_q:
        if flag_e:
            break
        r,c = to_e_q.popleft()
        # 다음 이동 방향 특정
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            # 이동가부 판단
            if 0 <= nr < len_row and 0 <= nc < len_col and new_maps[nr][nc] != "X" and not visit_to_e[nr][nc]:
                # 이동
                cnt_e[nr][nc] = cnt_e[r][c] + 1
                # 이동한게 "E"이면 그만 이동
                if new_maps[nr][nc] == "E":
                    e.append(nr)
                    e.append(nc)
                    flag_e = True
                    cnt_to_e = cnt_e[nr][nc]
                    break
                to_e_q.append([nr,nc])
                visit_to_e[nr][nc] = True
    # 이동 불가
    if not e:
        return -1
    return cnt_to_l + cnt_to_e