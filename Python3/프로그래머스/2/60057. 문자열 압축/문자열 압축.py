def zipper(s, part_len):
    idx = 0
    s_len = len(s)
    
    zipped = ''
    before = s[:part_len]
    cnt = 1
    
    idx = part_len
    
    while idx < s_len:
        cur = s[idx:idx + part_len]
        
        if cur == before:
            cnt += 1
        else:
            if cnt > 1:
                zipped += str(cnt)
            zipped += before
            before = cur
            cnt = 1
        idx += part_len
    if cnt > 1:
        zipped += str(cnt)
    zipped += before
    
    return len(zipped)
            

def solution(s):
    s_len = len(s)
    # 최대 압축은 1/2길이까지만 -> 이후는 1자리때랑 동일
    max_part = s_len // 2
    
    min_len = s_len
    
    for part_len in range(1, max_part + 1):
        zipped_len = zipper(s, part_len)
        min_len = min(min_len, zipped_len)
    
    return min_len
        