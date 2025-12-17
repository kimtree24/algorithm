import sys
input = sys.stdin.readline

n = int(input().strip())

# 최초 종이 입력
paper = []
for _ in range(n):
    line = list(map(int, input().strip().split()))
    paper.append(line)

# 결과트래킹(하양, 파랑)
result = [0,0]

def cut_paper(r, c, size):
    std = paper[r][c]
    flag = True
    
    # 탈출조건
    for row in range(r, r + size):
        for col in range(c, c + size):
            if paper[row][col] != std:
                flag = False
                break
        if not flag:
            break
            
    if flag:
        result[std] += 1
        return
    else:
        new_size = size // 2
        for row in range(2):
            for col in range(2):
                cut_paper(r + row * new_size, c + col * new_size, new_size)
cut_paper(0,0,n)
print(result[0])
print(result[1])