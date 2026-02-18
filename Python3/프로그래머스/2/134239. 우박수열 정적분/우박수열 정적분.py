def cal_area(start, end):
    s_x, s_y = start
    e_x, e_y = end
    
    x_len = e_x - s_x
    tr_h = max(s_y, e_y) - min(s_y, e_y)
    rac_h = min(s_y, e_y)
    
    area = (x_len * tr_h / 2) + (x_len * rac_h)
    return area

def get_wooback(k):
    wooback = []
    idx = 0
    
    wooback.append((idx, k))
    
    while k > 1:
        if k % 2 == 0:
            k = k // 2
        else:
            k = k * 3 + 1
        idx += 1
        wooback.append((idx, k))
    return wooback

def solution(k, ranges):
    # 좌표 구하기
    # 적분 계산 식 구하기
    # 적분 하기 전에 구간 밸리데이션 치기
    
    ans = []
    
    wooback = get_wooback(k)
    
    for each_range in ranges:
        sx = each_range[0]
        ex = wooback[-1][0] + each_range[1]
        
        # 밸리데이션
        if sx > ex:
            ans.append(-1)
        else:
            area = 0
            for start in range(sx, ex):
                end = start + 1
                area += cal_area((start,wooback[start][1]), (end,wooback[end][1]))
            ans.append(area)
    return ans
        