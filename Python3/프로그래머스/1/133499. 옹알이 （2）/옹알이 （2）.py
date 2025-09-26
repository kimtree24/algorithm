def solution(babbling):
    result = 0

    # 각 단어별 판단
    for word in babbling:
        # 이전 조각 트리거용
        prev = ''
        idx = 0
        trigger = True
        # 지금 판단 단어 순회
        while idx < len(word):
            can_speak = ['aya', 'ye', 'woo', 'ma']
            matched = False
            if not trigger:
                break
            for i in can_speak:
                if i == prev:
                    continue
                elif word[idx:].startswith(i):
                    prev = i
                    idx += len(i)
                    matched = True
                    break
            if not matched:
                trigger = False
        if trigger:
            result += 1
    
    return result
                    
                    