def solution(s):
    result = []
    i = 0
    while i < len(s):
        diff_cnt = 0
        same_cnt = 0
        s_idx = i
        while s_idx < len(s):
            if s[i] == s[s_idx]:
                same_cnt += 1
            else:
                diff_cnt += 1
            s_idx += 1
            if same_cnt == diff_cnt:
                break
        result.append(s[i:s_idx])
        i = s_idx
    return len(result)