from collections import deque

def solution(maps):
    ans = []
    mapX = len(maps[0])
    mapY = len(maps)
    
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    
    visited = [[False] * mapX for _ in range(mapY)]
    
    def bfs(x,y):
        count = int(maps[y][x])
        q = deque()
        q.append((x, y))
        visited[y][x] = True
        
        while q:
            x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= ny < mapY and 0 <= nx < mapX and not visited[ny][nx]:
                    if maps[ny][nx] != 'X':
                        visited[ny][nx] = True
                        q.append((nx, ny))
                        count += int(maps[ny][nx])
        return count
    

    for i in range(mapY):
        for j in range(mapX):
            if not visited[i][j] and maps[i][j] != 'X':
                result = bfs(j, i)
                ans.append(result)

    if not ans:
        return[-1]
    else:
        ans.sort()
        return ans